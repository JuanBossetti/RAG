import os


PDF_FOLDER = "/pdfs"
ZIP_FOLDER = "/zips"

class Routes:
    @staticmethod
    def get_zipRoute():
        BASE_PATH = os.getenv("BASE_PATH", "/mnt/datos/desarrollo/documentos/rag")
        USER_PATH = os.getenv("USER_PATH", "/all_files")
        zip_files = BASE_PATH + USER_PATH + ZIP_FOLDER
        return zip_files
    
    @staticmethod
    def get_pdfRoute():
        BASE_PATH = os.getenv("BASE_PATH", "/mnt/datos/desarrollo/documentos/rag")
        USER_PATH = os.getenv("USER_PATH", "/all_files")
        pdf_files = BASE_PATH + USER_PATH + PDF_FOLDER
        return pdf_files
