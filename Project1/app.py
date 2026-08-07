from langchain_community.vectorstores import Chroma
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.prompts import PromptTemplate

embeddings = OllamaEmbeddings(model="nomic-embed-text")

db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings,
)

retriever = db.as_retriever(search_kwargs={"k": 3})

llm = ChatOllama(
    model="llama3.1:8b",
    temperature=0,
)

prompt = PromptTemplate.from_template("""
You are an AI Assistant.

Answer ONLY using the provided context.

If the answer is not available, say:
"I don't know."

Context:
{context}

Question:
{question}
""")

while True:
    question = input("\nAsk Question: ")

    if question.lower() == "exit":
        break

    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    final_prompt = prompt.format(
        context=context,
        question=question,
    )

    response = llm.invoke(final_prompt)

    print("\nAnswer:\n")
    print(response.content)