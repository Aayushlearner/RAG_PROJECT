from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
import os
from dotenv import load_dotenv

load_dotenv()

# Load PDF file
file_path = r"/Users/aayushtiwari/Desktop/RAG/NIPS-2017-attention-is-all-you-need-Paper.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()

text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k_base", chunk_size=100, chunk_overlap=0
)

# Split text for all pages
all_texts = [text_splitter.split_text(doc.page_content) for doc in docs]

# Flatten the list (since each page gives a list of chunks)
all_texts = [chunk for page in all_texts for chunk in page]

# Initialize HuggingFace embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Generate embeddings for each text chunk
embedded_chunks = [embeddings.embed_query(chunk) for chunk in all_texts]

# Qdrant connection parameters
url = os.getenv("QDRANT_URL")
api_key = os.getenv("QDRANT_API_KEY")

# Store embeddings in Qdrant vector store
qdrant = QdrantVectorStore.from_documents(
    docs,
    embeddings,
    url=url,
    prefer_grpc=True,
    api_key=api_key,
    collection_name="my_documents",
)





