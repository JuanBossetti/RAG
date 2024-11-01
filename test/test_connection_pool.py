import requests
import concurrent.futures
import time
import uuid

API_URL = "http://localhost:6000/rag-api"

# Define un payload básico para enviar a la API.
def generate_payload():
    """
    Genera un payload con un UUID válido para la solicitud.
    """
    return {
        "pregunta": "¿Cuál es la capital de Francia?",
        "chain_uuid": str(uuid.uuid4())  # Genera un UUID válido.
    }

# Definir el número de solicitudes para probar la capacidad del pool.
NUM_REQUESTS = 25

def make_request():
    """
    Función que envía una solicitud POST a la API y retorna el código de estado.
    """
    payload = generate_payload()
    try:
        response = requests.post(API_URL, json=payload)
        print(f"Status Code: {response.status_code} - Response: {response.json()}")
        return response.status_code
    except Exception as e:
        print(f"Error al hacer la solicitud: {e}")
        return None

def test_api_response():
    """
    Prueba básica para verificar que la API responde correctamente.
    """
    print("Iniciando prueba básica de respuesta...")
    payload = generate_payload()
    response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
        print("Respuesta correcta:", response.json())
    else:
        print(f"Error en la respuesta, código de estado: {response.status_code}")

def test_concurrent_requests():
    """
    Realiza múltiples solicitudes concurrentes para probar el manejo del pool de conexiones.
    """
    print(f"Iniciando prueba con {NUM_REQUESTS} solicitudes concurrentes...")
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(make_request) for _ in range(NUM_REQUESTS)]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]

    end_time = time.time()
    print(f"Prueba de solicitudes concurrentes completada en {end_time - start_time:.2f} segundos.")
    print(f"Resultados: {results}")

    # Verifica que todas las respuestas sean 200.
    success_count = sum(1 for status in results if status == 200)
    print(f"Solicitudes exitosas: {success_count}/{NUM_REQUESTS}")

def test_connection_pool_exhaustion():
    """
    Prueba que el pool de conexiones no se agote al hacer más peticiones que el tamaño del pool.
    """
    print(f"Iniciando prueba de agotamiento del pool con {NUM_REQUESTS * 2} solicitudes...")
    start_time = time.time()

    # Realizar solicitudes concurrentes que excedan el tamaño del pool.
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(make_request) for _ in range(NUM_REQUESTS * 2)]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]

    end_time = time.time()
    print(f"Prueba de agotamiento del pool completada en {end_time - start_time:.2f} segundos.")
    print(f"Resultados: {results}")

    # Verifica que todas las respuestas sean 200.
    success_count = sum(1 for status in results if status == 200)
    print(f"Solicitudes exitosas: {success_count}/{NUM_REQUESTS * 2}")

if __name__ == "__main__":
    # Ejecutar las pruebas
    test_api_response()
    test_concurrent_requests()
    test_connection_pool_exhaustion()
