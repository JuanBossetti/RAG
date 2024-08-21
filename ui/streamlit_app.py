import streamlit as st
from api_client import APIClient
import uuid

# Generar un UUID único para cada pestaña abierta
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

def main():
    st.header("NeuralChat")

    # Mostrar el UUID único de la pestaña
    st.write(f"UUID: {st.session_state.uuid}")

    print_all_messages(st.session_state.messages)
    
    question = st.chat_input("Envía tu pregunta sobre FastPrg")
    if question:
        handle_chat_input(question)

if __name__ == "__main__":
    main()
