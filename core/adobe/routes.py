import os

BASE_PATH = os.getenv("BASE_PATH", "/mnt/datos/desarrollo/documentos")
PDF_PATH = os.getenv("PATH_PDF", "/mnt/datos/desarrollo/documentos/pdf")

# Rutas referidas al zip que generamos a partir del consumo de la api de adobe
zip_file = f"{PDF_PATH}/2"
input_pdf = f"{BASE_PATH}/origin_pdf"
temp_zip_file = "/tmp/ExtractTextInfoFromPDF.zip"

# Rutas referidas a los distintos archivos que se extraen del zip para generar los chunks
unzip_dir = f"{PDF_PATH}"
chunked_dir = f"{PDF_PATH}/chunks"
tables_dir = f"{PDF_PATH}/tables"
figures_dir = f"{PDF_PATH}/figures"
json_dir = f"{PDF_PATH}/structuredData.json"

class Routes:
    def get_zipRoute():
        return zip_file
    
    def get_pdfRoute():
        return input_pdf
    
    def get_tempZipRoute():
        return temp_zip_file
        
    def get_unzipDirRoute():
        return unzip_dir
    
    def get_chunkedDirRoute():
        return chunked_dir
    
    def get_tablesDirRoute():
        return tables_dir
    
    def get_figuresDirRoute():
        return figures_dir
    
    def get_jsonDirRoute():
        return json_dir
    
    # MÉTODOS AUXILIARES PARA BORRAR LA INFORMACIÓN EXTRAÍDA DEL ARCHIVO ZIP DURANTE LA CORRIDA
    def eliminar_contenido_carpeta(ruta):
        try:
            for elemento in os.listdir(ruta):
                elemento_ruta = os.path.join(ruta, elemento)
                if os.path.isfile(elemento_ruta):
                    os.unlink(elemento_ruta)
                elif os.path.isdir(elemento_ruta):
                    Routes.eliminar_contenido_carpeta(elemento_ruta)
            print(f"El contenido de la carpeta {ruta} ha sido eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar el contenido de la carpeta {ruta}: {e}")

    def eliminar_carpeta(ruta):
        try:
            os.system(f'rm -rf "{ruta}"')
            print(f"La carpeta o archivo {ruta} ha sido eliminada exitosamente.")
        except Exception as e:
            print(f"Error al eliminar la carpeta o el archivo {ruta}: {e}")