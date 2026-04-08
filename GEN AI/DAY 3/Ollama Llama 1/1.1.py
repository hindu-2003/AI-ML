import ollama

response = ollama.chat(
    model="llama3.2:latest",
    messages=[
        {"role": "user", "content": "Define AI"}
    ],
    stream=False  
)

print(response["message"]["content"])
