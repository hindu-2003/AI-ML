import requests

response = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "llama3.2:latest",
        "messages": [{"role": "user", "content": "Explain AI in simple terms."}],
        "stream": False  
    }
)
# print(response.json())

data = response.json()

print(data)

#print(data["message"]["content"])