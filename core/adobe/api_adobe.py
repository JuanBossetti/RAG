import traceback
from script_descarga import download_nltk_components
from retriever import PostgresDbManager
from adobe_extract import AdobeExtract
from splitter import process_multiple_zip
from flask import Flask, request, jsonify
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
    model_embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/gtr-t5-xxl")
    app.db_manager = PostgresDbManager(model_embedding)
    app.adobe_extract = AdobeExtract()
    download_nltk_components()
    return app


app = create_app()




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

    
@app.route('/clear_database', methods=['POST'])
def clear_database():
    try:
        app.db_manager.clear_collection_by_drop()
        return jsonify({"message": "All tables cleared successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500





if __name__ == '__main__':
    app.run(debug=False, port=4000)
