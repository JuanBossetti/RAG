import requests

url = 'http://127.0.0.1:4000/add_documents'  # Reemplaza 'tu-servidor' con la URL de tu servidor
headers = {'Content-Type': 'application/json'}
data = {
    "docs": ["Enterprise - Especificación Funcional - Registro de Eventos_03_07.pdf", "Enterprise - Especificación Funcional - Tipos de Atributos_03_07.pdf"]
        }

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Documentos agregados exitosamente")
else:
    print(f"Error al agregar documentos: {response.status_code}")
