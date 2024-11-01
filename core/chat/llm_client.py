from langchain_community.llms import Ollama
from langchain_groq import ChatGroq
from langchain_fireworks import ChatFireworks 
import os

#Enviar a distintas carpetas
#Cada modleo debe tener adentro su prompt template

class FireworksClient:
    _instance = None

    def __new__(cls, model_name="accounts/fireworks/models/llama-v3p1-70b-instruct"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # os.environ['FIREWORKS_API_KEY'] = "aWOTrhGEOHrPf0QKhB4yKp7oEoZVRQv3l0kOQ0vWk7nImlUu"
            cls._instance.llm = ChatFireworks(
            model=model_name,            
            temperature=0,
            max_tokens=11000,
        )
        return cls._instance.llm

class LLMClient:
    _instance = None

    def __new__(cls, model_name="llama3:70b-instruct", base_url="http://172.100.0.53:11434"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.llm = Ollama(model=model_name, base_url=base_url, temperature=0)
        return cls._instance.llm


class GroqClient:
    _instance = None

    def __new__(cls, model_name="llama3:70b-instruct"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # os.environ['GROQ_API_KEY'] = "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"
            cls._instance.llm = ChatGroq(temperature=0, model_name=model_name)
        return cls._instance.llm