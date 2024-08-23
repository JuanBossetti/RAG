import nltk
from nltk.data import find

def check_and_download_nltk_component(component):
    try:
        # Verifica si el componente ya está descargado
        find(f'tokenizers/{component}')
        print(f'{component} is already downloaded.')
    except LookupError:
        # Si no está descargado, lo descarga
        print(f'{component} is not downloaded. Downloading now...')
        nltk.download(component)
        print(f'{component} has been successfully downloaded.')

def download_nltk_components():
    check_and_download_nltk_component('punkt')
    check_and_download_nltk_component('punkt_tab')


