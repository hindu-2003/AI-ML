import ollama

# Context (Knowledge Source)

context = """
Machine learning is a subset of Artificial Intelligence (AI). It allows computer systems to learn patterns from data and improve their performance without being explicitly programmed.
Machine learning is widely used in applications such as recommendation systems, image recognition, and fraud detection.
"""


# User Question

question = "What is machine learning?"

# Prompt Construction

prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{question}

Answer:
"""

# Call Ollama Model

response = ollama.generate(
    model="llama3.2",
    prompt=prompt
)

# -----------------------------
# Print Model Output
# -----------------------------

print("\nAnswer:")
print(response["response"])