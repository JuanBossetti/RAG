
import os
import traceback
import shutil
import zipfile
import re
import pandas as pd
import json
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import NLTKTextSplitter


def process_multiple_zip(correctly_processed):
    correctly_chunked = []
    unchunked = []
    for cp in correctly_processed:
        try:
            chunks = process_zip(cp[1])
            correctly_chunked.append((cp[0], chunks))
        except Exception as e:
            exception_text = traceback.format_exc()
            unchunked.append((cp[0], exception_text))
    return correctly_chunked, unchunked




def process_zip(input_zip):

    if not input_zip.lower().endswith('.zip'):
        raise ValueError("No es un archivo zip valido")
    
    unzip_dir, chunked_dir = _prepare_directories(input_zip)

    _zip_file(input_zip, unzip_dir)
    json_file_path = os.path.join(unzip_dir, "structuredData.json")
    elements = _parse_json(json_file_path)

    file_split = 0
    FIRST_TIME_HEADER = True
    FIRST_TIME_HEADER2 = True
    FIRST_TIME_HEADER3 = True
    file_name = os.path.join(chunked_dir, f"file_{file_split}")
    parsed_file = open(file_name, "a", encoding="utf-8")

    for element in elements:
            if "//Document/H1" in element["Path"]:
                # Se extrae el texto del elemento y se almacena en la variable hdr_txt.
                hdr_txt = element["Text"]
                if FIRST_TIME_HEADER:
                    FIRST_TIME_HEADER = False
                    # Si es la primera vez que se encuentra la cabecera, se escribe en el archivo.
                    parsed_file.write(hdr_txt)
                    parsed_file.write("\n")
                    parsed_file.write(" ")
                else:
                    # Se cierra el archivo actual.
                    parsed_file.close()
                    file_split = file_split + 1
                    # Se crea el nombre del próximo archivo.
                    file_name = os.path.join(chunked_dir, f"file_{file_split}".format(file_split=file_split))
                    # Se abre el próximo archivo en modo de adición.
                    parsed_file = open(file_name, "a", encoding="utf-8")
                    # Se escribe la cabecera en el nuevo archivo.
                    parsed_file.write(hdr_txt)
                    parsed_file.write("\n")
                    parsed_file.write(" ")
            else:
                if "//Document/H2" in element["Path"]:
                    # Se extrae el texto del elemento y se almacena en la variable hdr_txt.
                    hdr_txt = element["Text"]
                    if FIRST_TIME_HEADER2:
                        FIRST_TIME_HEADER2 = False
                        # Si es la primera vez que se encuentra la cabecera, se escribe en el archivo.
                        parsed_file.write(hdr_txt)
                        parsed_file.write("\n")
                        parsed_file.write(" ")
                    else:
                        # Se cierra el archivo actual.
                        parsed_file.close()
                        file_split = file_split + 1
                        # Se crea el nombre del próximo archivo.
                        file_name = os.path.join(chunked_dir, f"file_{file_split}".format(file_split=file_split))
                        # Se abre el próximo archivo en modo de adición.
                        parsed_file = open(file_name, "a", encoding="utf-8")
                        # Se escribe la cabecera en el nuevo archivo.
                        parsed_file.write(hdr_txt)
                        parsed_file.write("\n")
                        parsed_file.write(" ")
                else:
                    if "//Document/H3" in element["Path"]:
                        # Se extrae el texto del elemento y se almacena en la variable hdr_txt.
                        hdr_txt = element["Text"]
                        if FIRST_TIME_HEADER3:
                            FIRST_TIME_HEADER3 = False
                            # Si es la primera vez que se encuentra la cabecera, se escribe en el archivo.
                            parsed_file.write(hdr_txt)
                            parsed_file.write("\n")
                            parsed_file.write(" ")
                        else:            
                            # Se cierra el archivo actual.
                            parsed_file.close()
                            file_split = file_split + 1
                            # Se crea el nombre del próximo archivo.
                            file_name = os.path.join(chunked_dir, f"file_{file_split}".format(file_split=file_split))
                            # Se abre el próximo archivo en modo de adición.
                            parsed_file = open(file_name, "a", encoding="utf-8")
                            # Se escribe la cabecera en el nuevo archivo.
                            parsed_file.write(hdr_txt)
                            parsed_file.write("\n")
                            parsed_file.write(" ")
                    else:
                        if "Document/Table" in element["Path"]:
                            match = re.search(r'^//Document/Table(?:\[\d+\])?$', element["Path"])
                            if match:
                                xlsx_file_name = element["filePaths"][0]
                                xlsx_file = os.path.join(unzip_dir, "", xlsx_file_name)
                                df = pd.DataFrame(pd.read_excel(xlsx_file))
                                table_content = df.to_markdown().replace("_x000D_", "      ")
                                parsed_file.write(table_content)
                                parsed_file.write("\n")
                                parsed_file.write(" ")
                        else:    
                            try:
                                text_content = element["Text"]
                                parsed_file.write(text_content)
                                parsed_file.write("\n")
                                parsed_file.write(" ")
                            except KeyError as ke:
                                pass

    parsed_file.close()

    files = _get_files_from_dir(chunked_dir)
    print("La cantidad de chunks generados a partir de las etiquetas del parseo del Json fueron: " + str(len(files)))
    
    list_of_all_docs = [_load_docs(file)[0] for file in files]

    chunks = _NLTK_splitter(list_of_all_docs)
    return chunks

def _prepare_directories(zip_file_path):
    # Obtener el directorio base y el nombre del archivo sin extensión
    base_dir = os.path.dirname(zip_file_path)
    file_name_without_ext = os.path.splitext(os.path.basename(zip_file_path))[0]

    # Construir las rutas a unzip_dir y chunked_dir
    unzip_dir = os.path.join(base_dir, file_name_without_ext, "unzip_dir")
    chunked_dir = os.path.join(base_dir, file_name_without_ext, "chunked_dir")

    # Función para asegurar que el directorio existe y está vacío
    def ensure_empty_dir(dir_path):
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
        os.makedirs(dir_path)

    # Asegurar que los directorios existen y están vacíos
    ensure_empty_dir(unzip_dir)
    ensure_empty_dir(chunked_dir)

    return unzip_dir, chunked_dir


def _zip_file(output_path, unzip_dir):
    with zipfile.ZipFile(output_path, 'r') as zip_ref:
        zip_ref.extractall(unzip_dir)


def _parse_json(json_file_path):
    with open(json_file_path, "r") as json_file:
        content = json.loads(json_file.read())
        pdf_element = content["elements"]
        return pdf_element

def _get_files_from_dir(dir):
    return [os.path.join(dir, f) for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]

def _load_docs(file_path):
    loader = TextLoader(file_path, encoding="utf-8")    
    return loader.load()

def _NLTK_splitter(list_of_docs):
    text_splitter = NLTKTextSplitter()
    pages = text_splitter.split_documents(list_of_docs)
    print("La cantidad final de chunks generados luego del NLTK Splitter fueron: " + str(len(pages)))
    return pages
