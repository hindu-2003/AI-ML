import ollama

stream1 = ollama.chat(
    model="llama3.2:latest",
    messages=[
        {"role": "user", "content": "Define AI"}
    ],
    stream=True
)

for chunk in stream1:
    print(chunk['message']['content'], end="", flush=True)
   

