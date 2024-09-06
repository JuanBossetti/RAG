import requests
import json


'''

url = 'http://127.0.0.1:4000/clear_database'  
headers = {'Content-Type': 'application/json'}
data = {}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Base limpiada exitosamente")
else:
    print(f"Error al limpiar la BD: {response.status_code}")

'''
url = 'http://127.0.0.1:4000/add_documents'  
headers = {'Content-Type': 'application/json'}
data = {
    "docs": ["Enterprise - Especificación Funcional - Registro de Eventos_03_07.pdf",
             #"Enterprise - Especificación Funcional - Tipos de Atributos_03_07.pdf",
             #"Enterprise - Especificación Funcional - Entidades_03_07.pdf",
             #"Enterprise - Especificación Funcional - Expresiones y Funciones.pdf",
             #"Enterprise – Especificación Funcional – Procesos de Negocio.pdf",
             #"Enterprise - Especificación Funcional - Seguridad_03_07.pdf"
             ]
        }

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    print("Documentos agregados exitosamente")
    print("Respuesta del servidor:")
    print(json.dumps(response.json(), indent=4))
else:
    print(f"Error al agregar documentos: {response.status_code}")
    print("Detalle del error:")
    print(json.dumps(response.json(), indent=4))
