import streamlit as st
import uuid
from api_client import APIClient

# Generar un UUID único para cada pestaña abierta
if 'uuid' not in st.session_state:
    st.session_state.uuid = str(uuid.uuid4())

# # Inicializar el cliente API y mensajes si no están en el estado de la sesión
# if "client" not in st.session_state:
#     st.session_state.client = APIClient()

if "messages" not in st.session_state:
    st.session_state.messages = []

def handle_chat_input(prompt):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("assistant"):
        response = "probando"
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

def print_all_messages(messages):
    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def main():
    st.header("NeuralChat")

    # Mostrar el UUID único de la pestaña
    st.write(f"UUID único para esta pestaña: {st.session_state.uuid}")

    print_all_messages(st.session_state.messages)
    
    prompt = st.chat_input("Envía tu pregunta sobre FastPrg")
    if prompt:
        handle_chat_input(prompt)

if __name__ == "__main__":
    main()