from prompt_provider import PromptProvider
from langchain_postgres import PostgresChatMessageHistory
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.runnables.history import RunnableWithMessageHistory
from langsmith import traceable
from retriever import PostgresDbManager
import json

# Pensar como podemos tener una chain con repregunta y una chain sin
#self.sync_connection.close() ¿Cuándo cerramos la conexión?? Debe ser un método dentro de retriever el que cierre la conexión
class Chain:

    def __init__(self, llm, retriever):
        
        ### Create the table schema (only needs to be done once)
        table_name = "chat_history"
        self.sync_connection = PostgresDbManager().get_connection_for_chat_history()
        PostgresChatMessageHistory.create_tables(self.sync_connection, table_name)
        
        ### Answer question ###
        qa_prompt = PromptProvider.get_rag_prompt()        
        question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

        rag_chain = create_retrieval_chain(retriever, question_answer_chain)

        def get_session_history(session_id: str) -> PostgresChatMessageHistory:
            return PostgresChatMessageHistory(
                table_name,
                session_id,
                sync_connection=self.sync_connection
            )

        self.conversational_rag_chain = RunnableWithMessageHistory(
            rag_chain,
            get_session_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer",
        )

    @traceable
    def get_answer(self, question, chain_uuid):
        response = self.conversational_rag_chain.invoke(
                {"input": question},
                config={"configurable": {"session_id": chain_uuid}},
            )
        answer = response ['answer']
        context = response ['context']
        docs = []
        for c in context:
            docs.append({'page_content': c.page_content, 'metadata': c.metadata['source']})
        return answer, docs