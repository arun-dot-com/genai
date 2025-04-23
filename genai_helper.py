%%writefile dev_helper.py
import requests

def query_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload)
    return response.json()["response"]

if __name__ == "__main__":
    print("🧠 DevHelperGPT – Code Assistant using LLaMA 3\n")
    while True:
        user_input = input("💬 Enter code or error (or type 'exit'): ")
        if user_input.lower() == 'exit':
            break
        result = query_ollama(f"Debug or explain this:\n{user_input}")
        print("\n🤖 LLaMA 3 Response:\n", result, "\n")
