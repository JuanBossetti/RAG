import streamlit as st
from api_client import APIClient
import uuid

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

def handle_chat_input(question):
    with st.chat_message("user"):
        st.markdown(question)
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("assistant"):
        prompt = {"pregunta": question, "chain_uuid": st.session_state.uuid}
        response = st.session_state.client.ask_question(prompt)
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

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






def main():
    st.header("FastPrg Chat")

    with st.sidebar:
        svg_path = "sources/Grulla.svg"  # Ruta de tu archivo SVG
        with open(svg_path, "r") as file:
            svg_content = file.read()
        st.markdown(f'<div style="text-align: left; width: 15%;">{svg_content}</div>', unsafe_allow_html=True)
        st.title("Base de conocimiento")
        st.write("(actualizada al 03/09/2024)")

        
        documents = ["Entidades",
                    "Expresiones y Funciones",
                    "Procesos de Negocio",
                    "Registro de Eventos",
                    "Reglas de Negocio",
                    "Seguridad",
                    "Tipos de Atributos",
                    "Versionado"] 
        for doc in documents:
            st.write(doc)

    # Mostrar el UUID único de la pestaña
    st.write(f"UUID: {st.session_state.uuid}")

    print_all_messages(st.session_state.messages)
    
    question = st.chat_input("Envía tu pregunta sobre FastPrg")
    if question:
        handle_chat_input(question)

    add_image_bottom_right('sources/powered_by.png')




if __name__ == "__main__":
    main()
