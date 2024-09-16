from langchain_huggingface.embeddings import HuggingFaceEmbeddings

class EmbeddingModel:
    #utilizar la ruta local en la que guardamos el modelo
    def __init__(self, model_name="sentence-transformers/gtr-t5-xxl"):
        self.embedding_model = HuggingFaceEmbeddings(model_name=model_name)
    
    def get(self):
        return self.embedding_model

