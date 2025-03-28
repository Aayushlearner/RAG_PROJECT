# RAG (Retrieval-Augmented Generation) Project

This project implements a Retrieval-Augmented Generation (RAG) system using Streamlit for the user interface, LangChain for document processing, and Qdrant for vector storage.

## Project Files

- `text_extract.py`: Handles PDF document loading, text splitting, and embedding generation
- `llm.py`: Contains the Groq LLM integration and Qdrant search functionality
- `streamlit_rag_interface.py`: Provides the Streamlit web interface for querying the RAG system

## Requirements

- Python 3.13
- Required packages listed in `requirements.txt`

## Setup Instructions

1. Clone this repository
2. Create a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create a `.env` file with the following environment variables:
   ```
   QDRANT_URL=your_qdrant_url
   QDRANT_API_KEY=your_qdrant_api_key
   GROQ_API_KEY=your_groq_api_key
   ```

## Running the Application

To start the Streamlit interface:
```
streamlit run streamlit_rag_interface.py
```

The application will be available at http://localhost:8501

## Usage

1. Enter your query in the text input field
2. The system will retrieve relevant information from the document store
3. The LLM will generate a response based on the query and retrieved context

## Configuration

- The PDF file path can be modified in `text_extract.py`
- The LLM model and parameters can be adjusted in `llm.py`

## Dependencies

- LangChain ecosystem
- Streamlit
- Qdrant
- Groq API

## License

This project is licensed under the MIT License.
