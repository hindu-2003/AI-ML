import ollama

embedding = ollama.embeddings(
    model="nomic-embed-text",
    prompt="Artificial Intelligence"
)

print(len(embedding["embedding"]))