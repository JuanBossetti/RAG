from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

class PromptProvider:

    def get_contextualize_prompt():
        #Ver desde donde se obtiene el string del prompt
        #Ver como formatear el promt en base al modelo que necesitamos
        contextualize_system_prompt = (
            "<|begin_of_text|><|start_header_id|>system<|end_header_id|>"
            "As a language processor, your task is to create a standalone question in "
            "Spanish based on a given chat history and the latest user question."
            "The standalone question should be understandable without the need for context from the chat history."
            "Your response should focus on formulating a clear and concise question "
            "that captures the essence of the user's query in Spanish, "
            "without providing an answer or requiring additional context.<|eot_id|>"
            "<|start_header_id|>user<|end_header_id|>"
        )
    
        contextualize_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", contextualize_system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )
    
        return contextualize_prompt
    
    def get_rag_prompt():
        
        rag_system_prompt = (
            "<|begin_of_text|><|start_header_id|>system<|end_header_id|>"
            "As an assistant for question-answering tasks, your goal is to provide "
            "concise and accurate answers in Spanish using the given pieces of context."
            "If you don't know the answer, simply state that you don't know."
            "Your responses should be clear, direct, and in Spanish.<|eot_id|>"
            "<|start_header_id|>user<|end_header_id|>"
            "Here are the pieces of retrieved context. Please use them to answer the question in Spanish."
            "{context}<|eot_id|>"
            "<|start_header_id|>assistant<|end_header_id|>"
        )

        rag_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", rag_system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )

        return rag_prompt