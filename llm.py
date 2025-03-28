from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from text_extract import qdrant

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

def search_qdrant(query):
    return qdrant.search(query, search_type="similarity")