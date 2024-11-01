import streamlit as st
from api_client import APIClient
import uuid
import re
from io import StringIO


st.set_page_config(
    page_title="FastPrg Chat",
    page_icon="sources/favicon-neuralsoft-150x150.png",
)


if 'uuid' not in st.session_state:
    st.session_state.uuid = str(uuid.uuid4())

if "client" not in st.session_state:
    st.session_state.client = APIClient()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chunks" not in st.session_state:
    st.session_state.chunks = []

def handle_chat_input(question):
    with st.chat_message("user"):
        st.markdown(question)
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("assistant"):
        prompt = {"pregunta": question, "chain_uuid": st.session_state.uuid}
        response, chunks = st.session_state.client.ask_question(prompt)
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.session_state.chunks = chunks
    save_to_txt()
    show_chunks()



def print_all_messages(messages):
    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def add_image_bottom_right(image_path):
    # Renderizamos la imagen usando st.image() en el flujo de Streamlit
    st.image(image_path, width=150)

    st.markdown(
        """
        <style>
        [data-testid="stImage"] {
            position: fixed;
            bottom: 10px;
            right: -250px; 
            margin: 0;  
            padding: 0; 
            z-index: 100;
            overflow: hidden; 
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def show_sidebar():
    with st.sidebar:
        svg_path = "sources/Grulla.svg"  # Ruta de tu archivo SVG
        with open(svg_path, "r") as file:
            svg_content = file.read()
        st.markdown(f'<div style="text-align: left; width: 15%;">{svg_content}</div>', unsafe_allow_html=True)
        st.title("Base de conocimiento")
        st.write("(actualizada al 03/09/2024)")

        document_names = ["Entidades",
                     "Expresiones y Funciones",
                     "Procesos de Negocio",
                     "Registro de Eventos",
                     "Reglas de Negocio",
                     "Seguridad",
                     "Tipos de Atributos",
                     "Versionado"] 
        for doc_name in document_names:
            st.write(doc_name)
        st.markdown("<hr>", unsafe_allow_html=True)


def show_chunks():
    with st.sidebar:


        if len(st.session_state.chunks) > 0:
            st.title("Fragmentos analizados en la última respuesta")
            for i, chunk in enumerate(st.session_state.chunks):
                metadata = chunk ['metadata']
                page_content = chunk['page_content']
                st.markdown("Número :" +str( i + 1))

                pattern = r'/([^/]+)/chunked_dir/file_(\d+)'
                match = re.search(pattern, metadata)
                if match:
                    st.markdown("Documento origen: "+ match.group(1))
                    st.markdown("ID: "+match.group(2))
                else:
                    st.markdown("Documento origen: "+ metadata)
                st.markdown("Contenido:")
                st.markdown(page_content)
                st.markdown("<hr>", unsafe_allow_html=True)

def get_buffer_contents():
    buffer = StringIO()

    buffer.write(f"UUID: {st.session_state.uuid}\n\n")
            
    buffer.write("Historial de conversación:\n")
    for message in st.session_state.messages:
        role = "User" if message["role"] == "user" else "Bot"
        buffer.write(f"{role}: {message['content']}\n")
        if role == "Bot":
            buffer.write("\n")

    buffer.write("\n\n-------------------------------------------------------------------------------")
    buffer.write("\nFragmentos analizados en la última respuesta:\n")
    for i, chunk in enumerate(st.session_state.chunks):
        metadata = chunk['metadata']
        page_content = chunk['page_content']
        pattern = r'/([^/]+)/chunked_dir/file_(\d+)'
        match = re.search(pattern, metadata)
        doc_info = f"Documento origen: {match.group(1)}, ID: {match.group(2)}" if match else f"Documento origen: {metadata}"
        buffer.write(f"\nNúmero: {i + 1}\n{doc_info}\nContenido:\n{page_content}\n")
            
    return buffer.getvalue()


def save_to_txt():
    with st.sidebar:

        
        st.download_button(
            label="Descargar Conversación",
            data=get_buffer_contents(),
            file_name=f"conversation_history{st.session_state.uuid}.md",
            mime="text/plain"
        )





def main():
    st.header("FastPrg Chat")

    st.write(f"UUID: {st.session_state.uuid}")

    show_sidebar()

    #save_to_txt()

    #show_chunks()

    print_all_messages(st.session_state.messages)
    
    question = st.chat_input("Envía tu pregunta sobre FastPrg")
    if question:
        handle_chat_input(question)

    add_image_bottom_right('sources/powered_by.png')


if __name__ == "__main__":
    main()
