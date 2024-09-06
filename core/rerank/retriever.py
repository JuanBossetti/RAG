from langchain_postgres import PGVector
from langchain_community.vectorstores import PGVector

#Hacer genérico
class PostgresDbManager:
    def __init__(self,
                 model_embedding,
                 connection ="postgresql+psycopg://langchain:langchain@localhost:5002/langchain",
                 collection_name = "my_docs",
                 k=25):

        self.vectorstore = PGVector(
            embedding_function=model_embedding,
            collection_name=collection_name,
            connection_string=connection,
            use_jsonb=True,
        )

        self.retriever = self.vectorstore.as_retriever(
            search_type="similarity",  
            search_kwargs={"k": k}
        )

    def get_chunks(self, question):
        docs = self.retriever.get_relevant_documents(question)
        return docs
    
    def get_retriever(self):
        return self.retriever
    
    def get_vectorstore(self):
        return self.vectorstore