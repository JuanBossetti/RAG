from langchain_postgres import PGVector
import os

#Hacer genérico
class PostgresDbManager:
    def __init__(self,
                model_embedding,
                connection_info=None,
                collection_name="my_docs",
                k=8):
        
        if connection_info is None:
            user = os.getenv("PG_USER", "default")
            password = os.getenv("PG_PASSWORD", "default")
            db = os.getenv("PG_DB", "default")
            port = os.getenv("PG_PORT", "5432")
            host = os.getenv("PG_HOST", "localhost")
            connection_info = f"postgresql+psycopg://{user}:{password}@{host}:{port}/{db}"
            print(connection_info)

        self.model_embedding = model_embedding
        self.connection_info = connection_info
        self.collection_name = collection_name
        self.k = k

        self.vectorstore = PGVector(
            embeddings=model_embedding,
            collection_name=collection_name,
            connection=connection_info,
            use_jsonb=True,
        )

        self.retriever = self.vectorstore.as_retriever(
            search_type="similarity",  
            search_kwargs={"k": k}
        )
    
    def get_retriever(self):
        return self.retriever
    
    def get_vectorstore(self):
        return self.vectorstore
    
    def add_documents(self, pages):
        self.vectorstore.add_documents(pages)   

    def clear_collection_by_drop(self):
        """Elimina la tabla y la reconstruye."""
        self.vectorstore.drop_tables()
        self.vectorstore.create_tables_if_not_exists()
