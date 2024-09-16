from langchain_postgres import PGVector
import os
import psycopg

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


class PostgresChatMessageHistoryManager:
    def __init__(self, connection_for_chat_history=None):
        
        if connection_for_chat_history is None:            
            user = os.getenv("PG_USER", "default")
            password = os.getenv("PG_PASSWORD", "default")
            db = os.getenv("PG_DB", "default")
            port = os.getenv("PG_PORT", "5432")
            host = os.getenv("PG_HOST", "localhost")
            connection_for_chat_history = f"dbname={db} user={user} host={host} password={password} port={port}"

        self.connection_for_chat_history = connection_for_chat_history
    
    def get_connection_for_chat_history(self):
        ### Establish a synchronous connection to the database (or use psycopg.AsyncConnection for async)  
        sync_connection = psycopg.connect(self.connection_for_chat_history)
        return sync_connection