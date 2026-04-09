from langchain.vectorstores import FAISS
from langchain.docstore.document import Document

def create_vector_store(data, embeddings):
    docs = [
        Document(page_content=item["title"] + " " + str(item["content"]))
        for item in data
    ]

    db = FAISS.from_documents(docs, embeddings)
    return db