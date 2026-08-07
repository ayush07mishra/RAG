# 📄 Chat with PDF using RAG (Retrieval-Augmented Generation)

A simple Retrieval-Augmented Generation (RAG) application that allows users to ask questions about a PDF document. The application extracts text from a PDF, generates embeddings, stores them in a Chroma vector database, retrieves the most relevant chunks based on the user's query, and generates context-aware answers using a local LLM powered by Ollama.

---

## 🚀 Features

* 📄 Load and process PDF documents
* ✂️ Automatically split documents into chunks
* 🧠 Generate embeddings using `nomic-embed-text`
* 🗂️ Store embeddings in ChromaDB
* 🔍 Semantic search using vector similarity
* 🤖 Answer questions using `Llama 3.1` via Ollama
* 💻 Fully local execution (No API key required)

---

## 🛠️ Tech Stack

* Python
* LangChain
* ChromaDB
* Ollama
* Llama 3.1
* Nomic Embed Text
* PyPDF

---

## 📁 Project Structure

```text
chat-with-pdf/
│
├── app.py                 # Query pipeline
├── ingest.py              # PDF ingestion and embedding generation
├── requirements.txt
│
├── data/
│   └── employee_handbook.pdf
│
└── chroma_db/             # Vector database
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/chat-with-pdf-rag.git
cd chat-with-pdf-rag
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📥 Install Ollama

Download Ollama from:

https://ollama.com/download

Pull the required models:

```bash
ollama pull llama3.1:8b
ollama pull nomic-embed-text
```

Start the Ollama server:

```bash
ollama serve
```

---

## 📄 Add Your PDF

Place your PDF inside the `data/` folder.

Example:

```text
data/
└── employee_handbook.pdf
```

---

## 🧠 Generate Embeddings

Run the ingestion pipeline:

```bash
python ingest.py
```

This will:

* Read the PDF
* Split it into chunks
* Generate embeddings
* Store them in ChromaDB

---

## 💬 Run the Chatbot

```bash
python app.py
```

Example:

```text
Ask Question:
How many paid leaves do employees get?

Answer:
Employees receive 20 paid leaves annually.
```

Type `exit` to close the application.

---

## 🔄 RAG Pipeline

```text
PDF
   │
   ▼
PyPDFLoader
   │
   ▼
Recursive Character Text Splitter
   │
   ▼
Ollama Embeddings (nomic-embed-text)
   │
   ▼
Chroma Vector Database
   │
   ▼
Retriever
   │
   ▼
Prompt Template
   │
   ▼
Llama 3.1 (Ollama)
   │
   ▼
Final Answer
```

---

## 📦 Dependencies

* langchain
* langchain-community
* langchain-ollama
* langchain-text-splitters
* chromadb
* pypdf
* streamlit
* ollama

---

## 🎯 Future Improvements

* Multi-PDF support
* Streamlit web interface
* Source citations
* Chat history
* Metadata filtering
* Hybrid search
* Re-ranking
* Conversation memory
* FastAPI backend
* Docker support
* Cloud deployment

---

## 📚 Learning Objectives

This project demonstrates the core concepts of a Retrieval-Augmented Generation (RAG) pipeline:

* PDF ingestion
* Text chunking
* Embedding generation
* Vector database creation
* Semantic retrieval
* Prompt construction
* LLM-based answer generation

---

## 👨‍💻 Author

**Ayush Mishra**

If you found this project helpful, consider giving it a ⭐ on GitHub.
