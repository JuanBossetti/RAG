from retriever import PostgresDbManager
from adobe_extract import AdobeExtract
from splitter import process_multiple_zip
from flask import Flask, request, jsonify
from langchain_community.embeddings import HuggingFaceEmbeddings
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
    print("App creada correctamente")
    return app

app = create_app()


@app.route('/add_documents', methods=['POST'])
def add_documents():
    data = request.get_json()
    inputs_pdf = data.get("docs")
    try:
        zip_paths = app.adobe_extract.get_multiple_pdf_path(inputs_pdf)
        chunks = process_multiple_zip(zip_paths)
        app.db_manager.add_documents(chunks)
        return jsonify({"message": "Document added successfully"}), 201
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    
@app.route('/clear_database', methods=['POST'])
def clear_database():
    try:
        app.db_manager.clear_collection_by_drop()
        return jsonify({"message": "All tables cleared successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500





if __name__ == '__main__':
    app.run(debug=False, port=4000)
