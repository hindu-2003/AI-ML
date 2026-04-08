import ollama

prompt = "Write 3 benefits of Artificial Intelligence"

response = ollama.generate(
    model="llama3.2:latest",
    prompt=prompt
)

print(response["response"])