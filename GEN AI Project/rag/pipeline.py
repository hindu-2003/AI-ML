from langchain.chat_models import ChatOpenAI

def generate_response(query, db):
    retriever = db.as_retriever()
    docs = retriever.get_relevant_documents(query)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    You are an AI assistant.
    
    User Query: {query}
    
    Context:
    {context}
    
    Generate a personalized feed with explanation.
    """

    llm = ChatOpenAI(temperature=0.7)
    response = llm.predict(prompt)

    return response