import ollama

def chatbot():
    
    print("Chatbot: Hi! Ask me anything (type 'quit' to exit).")
    messages = []

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'quit':
            break

        messages.append({"role": "user", "content": user_input})

        # Stream response
        print("Chatbot: ", end="", flush=True)
        
        full_reply = ""
        
        for part in ollama.chat(model="ganapathi:latest", messages=messages, stream=True):
            
            chunk = part['message']['content']
            print(chunk, end="", flush=True)
            full_reply += chunk

        print() 
        messages.append({"role": "assistant", "content": full_reply})

chatbot()
