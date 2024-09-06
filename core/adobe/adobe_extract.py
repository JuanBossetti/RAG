import os
import traceback
import shutil
from routes import Routes
from adobe.pdfservices.operation.auth.credentials import Credentials
from adobe.pdfservices.operation.exception.exceptions import ServiceApiException, ServiceUsageException, SdkException
from adobe.pdfservices.operation.execution_context import ExecutionContext
from adobe.pdfservices.operation.io.file_ref import FileRef
from adobe.pdfservices.operation.pdfops.extract_pdf_operation import ExtractPDFOperation
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_pdf_options import ExtractPDFOptions
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_element_type import ExtractElementType
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_renditions_element_type import ExtractRenditionsElementType


class AdobeExtract:

    def __init__(self):
        self.execution_context = ExecutionContext.create(self._build_credentials())
        self.zip_folder_path = Routes.get_zipRoute()
        self.pdf_folder_path = Routes.get_pdfRoute()


        self._ensure_directory_exists(self.zip_folder_path)
    
    def get_multiple_pdf_path(self, inputs_pdf):
        correctly_processed = []
        unprocessed = []
        for ip in inputs_pdf:
            try:
                processed_pdf_path = self._get_processed_pdf_path(ip)
                correctly_processed.append((ip, processed_pdf_path))
            except Exception as e:
                exception_text = traceback.format_exc()
                unprocessed.append((ip, exception_text))

        return correctly_processed, unprocessed

    def _get_processed_pdf_path(self, input_pdf):
        zip_path = self._get_zip_path(input_pdf)
        if os.path.isfile(zip_path):
            return zip_path
        else:
            self._process_pdf(input_pdf, zip_path)
            return zip_path


    def _get_zip_path(self, file_name):
        if not file_name.endswith('.pdf'):
            raise ValueError("The file name must end with '.pdf'.")
        
        name_without_extension = os.path.splitext(file_name)[0]
        complete_path = os.path.join(self.zip_folder_path, name_without_extension + '.zip')
        return complete_path
    
    def _get_full_path(self, pdf_name):
        return os.path.join(self.pdf_folder_path, pdf_name)
    


    def _build_credentials(self):
        return Credentials.service_principal_credentials_builder() \
            .with_client_id(os.getenv("ADOBE_CLIENT_ID")) \
            .with_client_secret(os.getenv("ADOBE_SECRET")) \
            .build()

    def _process_pdf(self, input_pdf, output_zip):
        #Procesa un solo archivo PDF.
        full_pdf_path = self._get_full_path(input_pdf)
        extract_pdf_operation = self._setup_extract_operation(full_pdf_path)
        result = extract_pdf_operation.execute(self.execution_context)
        self._save_result(result, output_zip)
    
    def _ensure_directory_exists(self, directory):
        print(directory)
        if not os.path.exists(directory):
            os.makedirs(directory)

    def _setup_extract_operation(self, full_pdf_path):
        extract_pdf_operation = ExtractPDFOperation.create_new()
        source = FileRef.create_from_local_file(full_pdf_path)
        extract_pdf_operation.set_input(source)

        extract_pdf_options: ExtractPDFOptions = ExtractPDFOptions.builder() \
            .with_elements_to_extract([ExtractElementType.TEXT, ExtractElementType.TABLES]) \
            .with_elements_to_extract_renditions([ExtractRenditionsElementType.TABLES, ExtractRenditionsElementType.FIGURES]) \
            .build()
        # Es posible extrar imagenes agregando un ExtractElementType
                
        extract_pdf_operation.set_options(extract_pdf_options)
        
        return extract_pdf_operation
    
    def _save_result(self, result, zip_file):
        temp_dir = "/tmp/adobe_service_temp"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        
        temp_path = os.path.join(temp_dir, os.path.basename(zip_file))
        result.save_as(temp_path)
        shutil.move(temp_path, zip_file)
        if os.path.exists(temp_path):
            os.remove(temp_path)
    #def _save_result(self, result, zip_file):
        #temp_zip_file = os.path.join(self.temp_folder_path, os.path.basename(zip_file))

        #if os.path.isfile(temp_zip_file):
        #    os.remove(temp_zip_file)
        
        #result.save_as(zip_file)
        #shutil.copy(temp_zip_file, zip_file)
        

