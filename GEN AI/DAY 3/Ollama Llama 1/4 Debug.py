import ollama

def debug_code(code):
    prompt = f"Explain and fix this Python error:\n```python\n{code}\n```"
    response = ollama.chat(
        model="llama3.2:latest",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']


buggy_code = """
    def add(a, b):
        return a + b
    print(add(5, '10'))
    """
print(debug_code(buggy_code))