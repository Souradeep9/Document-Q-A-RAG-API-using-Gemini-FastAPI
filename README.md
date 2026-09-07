# Document-Q-A-RAG-API-using-Gemini-FastAPI
AI-powered Document Q&amp;A API using RAG, Google Gemini, FAISS, LangChain, and FastAPI.
# Document Q&A RAG API using Gemini & FastAPI
An AI-powered Document Question Answering API built using Retrieval-Augmented Generation (RAG), Google Gemini, and FastAPI.

The application allows users to upload a document and ask questions about its content. The system retrieves the most relevant document chunks using vector similarity search and uses Gemini to generate a contextual answer.
# Features
📄 Upload documents through an API
🔍 Extract and process document text
✂️ Split documents into smaller chunks
🧠 Generate embeddings for document chunks
🗄️ Store and search embeddings using FAISS
🔎 Retrieve relevant document context
🤖 Generate answers using Google Gemini
⚡ FastAPI REST API
📚 RAG-based question answering
🔐 API-key based Gemini integration
🧩 Modular project structure
# Architecture
User │ ▼ FastAPI │ ├── Upload Document │ │ │ ▼ │ Text Extraction │ │ │ ▼ │ Text Chunking │ │ │ ▼ │ Embeddings │ │ │ ▼ │ FAISS │ └── Ask Question │ ▼ Query Embedding │ ▼ Similarity Search │ ▼ Relevant Documents │ ▼ Gemini LLM │ ▼ Final Answer
# Technologies Used
Technology	Purpose
Python	Backend development
FastAPI	REST API development
Google Gemini	Large Language Model
LangChain	RAG pipeline development
FAISS	Vector similarity search
Sentence Transformers / Embeddings	Text embeddings
PyPDF	PDF text extraction
Uvicorn	FastAPI server
Pydantic	Data validation
# Project Structure
Document-QA-RAG-API/ │ ├── app/ │ ├── __init__.py │ ├── main.py │ ├── rag.py │ ├── schemas.py │ └── ... │ ├── data/ │ └── documents/ │ ├── .env ├── .gitignore ├── requirements.txt └── README.md
# Installation
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/Document-QA-RAG-API.git
cd Document-QA-RAG-API
2. Create a virtual environment
python -m venv venv
3. Activate the environment

Windows:

venv\Scripts\activate

Linux/macOS:

source venv/bin/activate
4. Install dependencies
pip install -r requirements.txt
# Configure Gemini API Key
Create a .env file in the project root:

GEMINI_API_KEY=your_gemini_api_key

Important: Never upload your API key to GitHub.

Add .env to .gitignore:

.env
venv/
__pycache__/
*.pyc
# Run the Application
Start the FastAPI server:

uvicorn app.main:app --reload

The API will run at:

http://127.0.0.1:8000

Open Swagger API documentation:

http://127.0.0.1:8000/docs
# API Endpoints
Upload Document
POST /upload

Uploads and processes a document for question answering.

Ask a Question
POST /ask

Example request:

{
  "question": "What is the main topic of the document?"
}

Example response:

{
  "answer": "The document mainly discusses..."
}
# How RAG Works
The project follows these steps:

1. Document Ingestion

The user uploads a document through the FastAPI endpoint.

2. Text Extraction

Text is extracted from the uploaded document.

3. Chunking

The extracted text is divided into smaller chunks so that relevant information can be retrieved efficiently.

4. Embedding Generation

Each text chunk is converted into a numerical vector representation using an embedding model.

5. Vector Storage

The embeddings are stored in a FAISS vector database.

6. Query Processing

When the user asks a question, the question is converted into an embedding.

7. Retrieval

FAISS performs similarity search and retrieves the most relevant document chunks.

8. Generation

The retrieved context and user's question are passed to Google Gemini, which generates the final answer.

Question
   ↓
Embedding
   ↓
FAISS Similarity Search
   ↓
Relevant Context
   ↓
Gemini
   ↓
Answer
# Example Use Case
A user uploads a company policy PDF and asks:

"What is the leave policy?"

Instead of sending the entire document to the LLM, the RAG pipeline:

Searches the document
Retrieves the relevant leave-policy sections
Sends those sections as context to Gemini
Generates an answer based on the retrieved information
# Key Learning Outcomes
Through this project, I worked with:

Retrieval-Augmented Generation (RAG)
Large Language Models (LLMs)
Google Gemini API
Vector databases
Semantic search
Text chunking
Embeddings
Prompt engineering
FastAPI
REST API development
Document processing
Python backend development
