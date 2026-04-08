import streamlit as st
import faiss
import pickle
import google.generativeai as genai
from sentence_transformers import SentenceTransformer


# GEMINI API
genai.configure(api_key="AIzaSyAS1UXcdMsEwuqTqTWuhCGDDq2607haujE")
model = genai.GenerativeModel("gemini-2.5-flash")


# EMBEDDING MODEL
embedder = SentenceTransformer("all-MiniLM-L6-v2")


# LOAD INDEX
index = faiss.read_index("medical.index")

with open("medical_docs.pkl", "rb") as f:
    docs = pickle.load(f)


# RETRIEVAL
def retrieve(query, top_k=3):

    query_vec = embedder.encode([query])

    distances, indices = index.search(query_vec, top_k)

    results = []

    for i in indices[0]:
        results.append(docs[i])

    return results


# RAG
def medical_assistant(query):

    retrieved_docs = retrieve(query)

    context = ""

    sources = set()

    for i, doc in enumerate(retrieved_docs):

        context += f"[{i+1}] {doc['text']}\n\n"

        sources.add(doc["source"])


    prompt = f"""
You are a medical knowledge assistant.

Answer only using the provided context.

Context:
{context}

Question:
{query}

If the answer is not in the context say "I don't know".
"""

    response = model.generate_content(prompt)

    return response.text, sources


# STREAMLIT UI

st.title("🩺 Medical Knowledge Assistant")

st.write("Ask questions from your medical documents")

query = st.text_input("Enter Medical Question")

if st.button("Ask"):

    answer, sources = medical_assistant(query)

    st.subheader("Answer")

    st.write(answer)

    st.subheader("Sources")

    for s in sources:
        st.write(s)