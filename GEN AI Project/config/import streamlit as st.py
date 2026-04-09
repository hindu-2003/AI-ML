import streamlit as st
from ingestion.fetch_data import fetch_ai_news
from embeddings.embedder import get_embeddings
from vectorstore.faiss_store import create_vector_store
from rag.pipeline import generate_response
from utils.helpers import format_output

st.set_page_config(page_title="AI Personalized Feed")

st.title("🔥 Real-Time AI Feed (RAG + GenAI)")

query = st.text_input("Ask something:", "Latest AI trends")

if st.button("Generate Feed"):
    with st.spinner("Fetching data..."):
        data = fetch_ai_news()

    with st.spinner("Creating embeddings..."):
        embeddings = get_embeddings()
        db = create_vector_store(data, embeddings)

    with st.spinner("Generating response..."):
        result = generate_response(query, db)

    st.success("Done!")
    st.write(format_output(result))