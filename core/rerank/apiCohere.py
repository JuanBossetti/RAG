import cohere
import time
from flask import Flask
from retriever import PostgresDbManager
from langchain_community.embeddings import HuggingFaceEmbeddings
import pandas as pd
from tabulate import tabulate

app = Flask(__name__)

def rerank():

    # Instanciamos el cliente Cohere con la api key
    co = cohere.Client("nMnc0x3TToq4q79qGALJmUVksu2DRkyAVbLlmciB")
    
    # Instanciamos la base de datos
    single_doc_embedding_model = embedding()

    # Nos traemos los chunks de una pregunta particular
    question = "¿Cuál es la diferencia entre consumir dispositivos por regla de negocio y consumirlos mediante una función?"
    chunks = PostgresDbManager(single_doc_embedding_model).get_chunks(question)
    print("La cantidad de chunks analizados es: ",len(chunks))

    # Generamos una lista de tipo String con el contenido de los chunks
    docsFast = []
    for chunk in chunks:
        docsFast.append(chunk.page_content)

    # Definimos el número de chunks relevantes que tendremos en cuenta tras su rerankeo
    top_chunks = 6

    response = co.rerank(
        # Modelo para documentos en inglés. Nosotros utilizaremos el modelo: model="rerank-multilingual-v3.0" 
        model="rerank-multilingual-v3.0",
        # Definición de la pregunta a partir de la cual el modelo buscará el documento que más información contenga de la misma
        query=question,
        # Listado de las 5 sentencias con descripciones de regiones o ciudades de Estados Unidos"
        documents=docsFast,
        # Indicación para que la respuesta contenga las 3 sentencias más relevantes, ordenadas desde la más relevante a la menos (score más cercano a 1, indica mayor relevancia)
        top_n=top_chunks,
        # Permite visualizar dentro del objeto response, los chunks seleccionados como más relevantes
        return_documents=True,
    )

    # El objeto response contiene una gran variedad de información. 
    # De la siguiente forma, sólo vamos a quedarnos con c/u de los documentos y su score, ya que será la información relevante para nosotros.
    
    # 1.Extraemos los textos rerankeados
    reranked_texts = [{'Text':docsFast[result.index], 'Score':result.relevance_score} for result in response.results]

    # 2.Ajusta las opciones de pandas para mostrar más caracteres en la consola. Si se establece None, no se define un límite
    pd.set_option('display.max_colwidth', None) 

    # 3.Mostramos los textos reordenados
    print("Textos mejor clasificados según la consulta: ", question)
    df = pd.DataFrame(reranked_texts)

    # 4.Convertir el DataFrame a formato Markdown, para una mejor visualización de cada uno de los textos en formato tabla
    markdown_table = tabulate(df.head(top_chunks), headers='keys', tablefmt='grid')
    print(markdown_table)

# MODELO EMBEDDING
def embedding():    
    # Selección del model embedding
    model_embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/gtr-t5-xxl")
    return model_embedding

@app.route('/rag-api/consumo_rerank', methods=['GET'])
def bd_postgres():
    start_time = time.time()
    rerank()
    elapsed_time = time.time() - start_time    
    print("El consumo del modelo de Rerank tardo ", elapsed_time, " segundos")
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
