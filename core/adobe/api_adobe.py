import json
import os
import traceback
from script_descarga import download_nltk_components
from retriever import PostgresDbManager
from adobe_extract import AdobeExtract
from splitter import process_multiple_zip
from routes import Routes
from flask import Flask, request, render_template, redirect, url_for, send_from_directory, jsonify
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv




def is_running_in_docker():
    #Determina si el proceso está corriendo dentro de un contenedor Docker.
    try:
        with open('/proc/1/cgroup', 'rt') as ifh:
            return 'docker' in ifh.read()
    except FileNotFoundError:
        return False

if not is_running_in_docker():
    # Configuración para el entorno local
    load_dotenv() # Carga variables de entorno del archivo .env


def create_app():
    app = Flask(__name__)
    app.db_manager = None
    app.adobe_extract = AdobeExtract()
    PDF_FOLDER = Routes.get_pdfRoute()
    ZIP_FOLDER = Routes.get_zipRoute()
    app.config['PDF_FOLDER'] = PDF_FOLDER
    app.config['ZIP_FOLDER'] = ZIP_FOLDER
    os.makedirs(PDF_FOLDER, exist_ok=True)
    os.makedirs(ZIP_FOLDER, exist_ok=True)
    download_nltk_components()
    return app





app = create_app()


@app.route('/initialize_db', methods=['POST'])
def initialize_db():
    try:
        model_embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/gtr-t5-xxl")
        app.db_manager = PostgresDbManager(model_embedding)
        return redirect(url_for('index'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    # Lista de archivos PDF en el directorio de subida
    pdf_files = [f for f in os.listdir(app.config['PDF_FOLDER']) if f.endswith('.pdf')]
    # Lista de archivos ZIP en el directorio de zips
    zip_files = [f for f in os.listdir(app.config['ZIP_FOLDER']) if f.endswith('.zip')]
    # Lista de archivos TXT en el directorio TXT_FOLDER
    txt_files = [f for f in os.listdir(app.config['ZIP_FOLDER']) if f.endswith('.txt')]
    return render_template('index.html', pdf_files=pdf_files, zip_files=zip_files, txt_files=txt_files)

@app.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    if 'pdf_file' not in request.files:
        return 'No file part'
    
    file = request.files['pdf_file']
    
    if file.filename == '':
        return 'No selected file'
    
    if file and file.filename.endswith('.pdf'):
        # Guarda el archivo en el directorio configurado
        file_path = os.path.join(app.config['PDF_FOLDER'], file.filename)
        file.save(file_path)
        return redirect(url_for('index'))
    else:
        return 'Invalid file type. Please upload a PDF.'


@app.route('/upload_zip', methods=['POST'])
def upload_zip():
    if 'zip_file' not in request.files:
        return 'No file part'
    
    file = request.files['zip_file']
    
    if file.filename == '':
        return 'No selected file'
    
    if file and file.filename.endswith('.zip'):
        # Guarda el archivo en el directorio configurado
        file_path = os.path.join(app.config['ZIP_FOLDER'], file.filename)
        file.save(file_path)
        return redirect(url_for('index'))
    else:
        return 'Invalid file type. Please upload a ZIP file.'


@app.route('/delete_pdf', methods=['POST'])
def delete_pdf():
    pdf_to_delete = request.form['pdf_to_delete']
    file_path = os.path.join(app.config['PDF_FOLDER'], pdf_to_delete)
    zip_to_delete = pdf_to_delete.replace('.pdf','.zip')
    zip_file_path = os.path.join(app.config['ZIP_FOLDER'], zip_to_delete)
    txt_to_delete = zip_to_delete.replace('.zip', '.txt')
    txt_file_path = os.path.join(app.config['ZIP_FOLDER'], txt_to_delete)
    
    if os.path.exists(file_path):
        os.remove(file_path)
        if os.path.exists(zip_file_path):
            os.remove(zip_file_path)
            if os.path.exists(txt_file_path):
                os.remove(txt_file_path)
            return redirect(url_for('index'))
    else:
        return 'File not found', 404

@app.route('/delete_zip', methods=['POST'])
def delete_zip():
    zip_to_delete = request.form['zip_to_delete']
    file_path = os.path.join(app.config['ZIP_FOLDER'], zip_to_delete)
    txt_to_delete = zip_to_delete.replace('.zip', '.txt')
    txt_file_path = os.path.join(app.config['ZIP_FOLDER'], txt_to_delete)

    if os.path.exists(file_path):
        os.remove(file_path)
        if os.path.exists(txt_file_path):
            os.remove(txt_file_path)
        return redirect(url_for('index'))
    else:
        return 'Zip File not found', 404


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['PDF_FOLDER'], filename)

@app.route('/zips/<filename>')
def view_zip(filename):
    return send_from_directory(app.config['ZIP_FOLDER'], filename)

@app.route('/txts/<filename>')
def view_txt(filename):
    return send_from_directory(app.config['ZIP_FOLDER'], filename)


@app.route('/add_documents', methods=['POST'])
def add_documents():
    data = request.get_json()
    inputs_pdf = data.get("docs")
    response = {
        "processed_documents": [],
        "unprocessed_documents": [],
        "chunked_documents": [],
        "unchunked_documents": [],
        "errors": []
    }

    try:
        correctly_processed, unprocessed = app.adobe_extract.get_multiple_pdf_path(inputs_pdf)

        # Documentos que no pudieron ser procesados por get_multiple_pdf_path
        for doc, error in unprocessed:
            response["unprocessed_documents"].append({
                "document": doc,
                "error": error
            })

        correctly_chunked, unchunked = process_multiple_zip(correctly_processed)

        # Documentos que fueron procesados correctamente
        for doc, processed_pdf_path in correctly_processed:
            response["processed_documents"].append({
                "document": doc,
                "processed_path": processed_pdf_path
            })

        # Documentos que no pudieron ser procesados en chunks
        for doc, error in unchunked:
            response["unchunked_documents"].append({
                "document": doc,
                "error": error
            })

        # Documentos que fueron chunked correctamente y añadidos a la base de datos
        for doc, chunks in correctly_chunked:
            app.db_manager.add_documents(chunks)
            response["chunked_documents"].append({
                "document": doc,
                "chunks": len(chunks)
            })

        return jsonify(response), 201

    except Exception as e:
        exception_text = traceback.format_exc()
        response["errors"].append({
            "message": str(e),
            "traceback": exception_text
        })
        return jsonify(response), 500
    

@app.route('/process_all_pdfs', methods=['POST'])
def process_all_pdfs():
    response = {
        "processed_documents": [],
        "unprocessed_documents": [],
        "chunked_documents": [],
        "unchunked_documents": [],
        "errors": []
    }

    try:
        # Obtener la lista de todos los PDFs en la carpeta configurada
        pdf_folder = app.config['PDF_FOLDER']
        pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
        
        # Procesar los archivos PDF
        correctly_processed, unprocessed = app.adobe_extract.get_multiple_pdf_path(pdf_files)

        # Documentos que no pudieron ser procesados por get_multiple_pdf_path
        for doc, error in unprocessed:
            response["unprocessed_documents"].append({
                "document": doc,
                "error": error
            })

        correctly_chunked, unchunked = process_multiple_zip(correctly_processed)

        # Documentos que fueron procesados correctamente
        for doc, processed_pdf_path in correctly_processed:
            response["processed_documents"].append({
                "document": doc,
                "processed_path": processed_pdf_path
            })

        # Documentos que no pudieron ser procesados en chunks
        for doc, error in unchunked:
            response["unchunked_documents"].append({
                "document": doc,
                "error": error
            })

        # Documentos que fueron chunked correctamente y añadidos a la base de datos
        for doc, chunks in correctly_chunked:
            app.db_manager.add_documents(chunks)
            response["chunked_documents"].append({
                "document": doc,
                "chunks": len(chunks)
            })

        return jsonify(response), 201

    except Exception as e:
        exception_text = traceback.format_exc()
        response["errors"].append({
            "message": str(e),
            "traceback": exception_text
        })
        return jsonify(response), 500

    

    
@app.route('/clear_database', methods=['POST'])
def clear_database():
    try:
        app.db_manager.clear_collection_by_drop()
        return jsonify({"message": "All tables cleared successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500





if __name__ == '__main__':
    app.run(debug=False, port=4000)
