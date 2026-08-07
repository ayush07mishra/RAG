from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

loader = PyPDFLoader("data/employee_handbook.pdf")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

docs = splitter.split_documents(documents)

embeddings = OllamaEmbeddings(model="nomic-embed-text")

db = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="chroma_db",
)

db.persist()

print("Embeddings stored successfully!")