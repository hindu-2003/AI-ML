import ollama
from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def summarize(text):
    prompt = f''' Act as a senior data summarizer. 
     Explain Life cycle of ML/DS application with  Data Preparation . 

{text}

For each stage include:
- objective
- Key Activities

Present the answer in a table.'''
    
    
    response = ollama.chat(
        model="llama3.2:latest",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']

if __name__ == "__main__":
    text = extract_text_from_pdf("Life Cycle.pdf")
    summary = summarize(text)
    print("Summary:\n", summary)