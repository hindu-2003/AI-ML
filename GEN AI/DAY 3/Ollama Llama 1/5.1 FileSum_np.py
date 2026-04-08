import ollama

file_path = input("Enter the file name: ")
model = "llama3.2:3b"

with open(file_path, 'r', encoding="utf-8") as file:
    content = file.read()

prompt = f"Give Applications of Machine Learning from given context only:\n\n{content}"

response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])

print("\nSummary:\n", response['message']['content'])
