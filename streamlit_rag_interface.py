import streamlit as st
from llm import llm, search_qdrant
from text_extract import qdrant

st.title('RAG LLM Interface')

user_query = st.text_input('Enter your query:')
if user_query:
    relevant_info = search_qdrant(user_query)
    messages = [
        ("system", "You are a helpful assistant "),
        ("human", user_query),
        ("system", f"Context from Qdrant: {relevant_info}")
    ]
    ai_msg = llm.invoke(messages)
    st.write(ai_msg.content)