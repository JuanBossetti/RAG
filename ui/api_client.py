import requests
import os
from dotenv import load_dotenv

load_dotenv() # Carga variables de entorno del archivo .env

class APIClient:
    def __init__(self, url=os.getenv("API_CHAT")):
        self.url = url

    def ask_question(self, prompt):
        try:
            headers = {"Content-Type": "application/json"}
            response = requests.post(self.url, json=prompt, headers=headers)
            response.raise_for_status()
            response_dict = response.json()
            text = response_dict["text"]
            return text
        except Exception as e:
            return "Se ha producido un error inesperado"