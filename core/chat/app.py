import time
from embedding_model import EmbeddingModel
from llm_client import LLMClient, GroqClient, FireworksClient
from chain import Chain
from retriever import PostgresDbManager
from flask import Flask, request
from dotenv import load_dotenv
import os

app = Flask(__name__)

def is_running_in_docker():
    """Determina si el proceso está corriendo dentro de un contenedor Docker."""
    try:
        with open('/proc/1/cgroup', 'rt') as ifh:
            return 'docker' in ifh.read()
    except FileNotFoundError:
        return False

if not is_running_in_docker():
    # Configuración para el entorno local
    # print("Carga variables de entorno del archivo .env")
    load_dotenv()

fireworks_client = FireworksClient()  #convertir a clase generica llmclient
single_doc_embedding_model = EmbeddingModel().get() #definir donde lo guardamos
db_manager = PostgresDbManager(single_doc_embedding_model)
#definir nombre de la clase para describir su fucnionalidad
#definir como trabjar con multiusuario
#definir como desactivar repregunta

@app.route('/rag-api', methods=['POST'])
def app_api():
    retriever = db_manager.get_retriever()
    chain = Chain(fireworks_client, retriever)
    pregunta = request.get_json()["pregunta"]
    chain_uuid = request.get_json()["chain_uuid"]
    print(chain_uuid)
    print(pregunta)
    infer_start_time = time.time()        
    ans, docs = chain.get_answer(pregunta, chain_uuid)
    infer_time = time.time() - infer_start_time
    print("Tiempo de ejecución de obtener la respuesta:", infer_time)
    
    answer = {}
    answer['text'] = ans
    answer['pregunta'] = pregunta    
    answer['infer_time'] = infer_time
    answer['docs'] = docs
    return answer


if __name__ == '__main__':
    app.run(debug=True, port=6000)  