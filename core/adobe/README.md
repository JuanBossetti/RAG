# Document Processing API

Esta API permite procesar documentos PDF y almacenarlos en una base de datos vectorial. Cuenta con dos endpoints principales: `add_documents` y `clear_database`.

## Endpoints

### 1. `POST /add_documents`
Este endpoint recibe una lista de nombres de documentos en formato PDF y los procesa de la siguiente manera:

- **Obtención de rutas de zips**: Verifica si ya existe un archivo zip correspondiente al PDF. Si existe, lo devuelve; si no, utiliza la API de Adobe para generarlo.
- **División en chunks**: Divide el contenido del documento en segmentos o "chunks".
- **Almacenamiento en base de datos vectorial**: Los chunks se envían y almacenan en una base de datos vectorial para facilitar búsquedas y análisis posteriores.

Retorna un informe detallado del procesamiento del documento con la siguiente informacion:

- **Documentos procesados exitosamente**: Lista de documentos que fueron procesados y chunked con éxito, junto con el número de chunks generados para cada uno.
- **Documentos no procesados**: Lista de documentos que no pudieron ser procesados inicialmente, incluyendo los errores específicos que ocurrieron.
- **Documentos chunked exitosamente**: Lista de documentos que fueron chunked con éxito, pero no necesariamente añadidos a la base de datos.
- **Documentos no chunked**: Lista de documentos que no pudieron ser chunked, con detalles de los errores.


#### Ejemplo de solicitud:
```json
{
  "docs": ["document1.pdf", "document2.pdf"]
}
```

#### Ejemplo de respuesta:
```json


{
  "processed_documents": [
    {
      "document": "document1.pdf",
      "processed_path": "/path/to/processed/document1.pdf"
    }
  ],
  "unprocessed_documents": [
    {
      "document": "document2.pdf",
      "error": "Error message or stack trace"
    }
  ],
  "chunked_documents": [
    {
      "document": "document1.pdf",
      "chunks": 5
    }
  ],
  "unchunked_documents": [
    {
      "document": "document1.pdf",
      "error": "Error message or stack trace"
    }
  ],
  "errors": []
}
```

### 2. POST /clear_database
Este endpoint permite limpiar todas las tablas de la base de datos vectorial.

#### Respuestas:
200 OK: Base de datos limpiada exitosamente.
500 Internal Server Error: Error al intentar limpiar la base de datos.


## Configuración
Variables de Entorno
El programa utiliza un archivo .env para configurar las siguientes variables de entorno:

PG_USER: Usuario de la base de datos PostgreSQL.
PG_PASSWORD: Contraseña de la base de datos PostgreSQL.
PG_DB: Nombre de la base de datos PostgreSQL.
PG_PORT: Puerto de conexión a PostgreSQL.
ADOBE_CLIENT_ID: ID de cliente para la API de Adobe.
ADOBE_SECRET: Secreto de cliente para la API de Adobe.
BASE_PATH: Ruta en la que buscará las carpetas que contienen los pdfs a procesar. Por defecto /mnt/datos/desarrollo/documentos/rag
USER_PATH: Sub directorio de BASE_PATH en la que buscará las subcarpetas "/pdfs" y "/zips". Por defecto /all_files

## Ejecución
Para ejecutar la aplicación, simplemente usa:

``` bash
python api_adobe.py
```

La API estará disponible en http://localhost:4000.
