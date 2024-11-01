from langchain_postgres import PGVector
import os
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from sqlalchemy.engine.url import URL
import psycopg

class PostgresDbManager:
    _instance = None  # Variable de clase para almacenar la única instancia
    _initialized = False  # Bandera para evitar re-inicialización

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # Si no existe una instancia, se crea una nueva
            cls._instance = super(PostgresDbManager, cls).__new__(cls)
        return cls._instance

    def __init__(
        self,
        model_embedding= None,
        connection_info=None,
        collection_name="my_docs",
        k=8,
    ):
        if self.__class__._initialized:
            # Si ya está inicializado, no se hace nada
            return

        if connection_info is None:
            user = os.getenv("PG_USER", "default")
            password = os.getenv("PG_PASSWORD", "default")
            db = os.getenv("PG_DB", "default")
            port = os.getenv("PG_PORT", "5432")
            host = os.getenv("PG_HOST", "localhost")
            
            # Crear la URL de conexión para SQLAlchemy
            conn_str = URL.create(
                drivername="postgresql+psycopg",
                username=user,
                password=password,
                host=host,
                port=port,
                database=db,
            )
            
            # Crear la cadena de conexión para psycopg
            self.connection_for_chat_history = f"dbname={db} user={user} host={host} password={password} port={port}"
        else:
            # Asumiendo que connection_info es una URL de SQLAlchemy
            conn_url = URL.create(connection_info)
            conn_str = conn_url
            
            # Extraer los componentes para crear la cadena de conexión de psycopg
            user = conn_url.username
            password = conn_url.password
            db = conn_url.database
            host = conn_url.host
            port = conn_url.port
            self.connection_for_chat_history = f"dbname={db} user={user} host={host} password={password} port={port}"

        self.model_embedding = model_embedding
        self.collection_name = collection_name
        self.k = k

        # Crear el engine con un pool de conexiones de SQLAlchemy
        self.engine = create_engine(
            conn_str,
            pool_size=20,
            max_overflow=5,
            poolclass=QueuePool,
        )

        # Usar el engine en PGVector
        self.vectorstore = PGVector(
            embeddings=model_embedding,
            collection_name=collection_name,
            connection=self.engine,
            use_jsonb=True,
        )

        self.__class__._initialized = True  # Marcar como inicializado

    def get_retriever(self):
        # Construir una nueva instancia del retriever
        retriever = self.vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": self.k},
        )
        return retriever

    def get_vectorstore(self):
        return self.vectorstore

    def add_documents(self, pages):
        self.vectorstore.add_documents(pages)

    def get_connection_for_chat_history(self):
        # ver la forma de usar el pool (engine) que creamos en el método init
        sync_connection = psycopg.connect(self.connection_for_chat_history)
        return sync_connection
