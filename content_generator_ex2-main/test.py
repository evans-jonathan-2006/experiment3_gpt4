import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "Explain Artificial Intelligence in 3 sentences."
        }
    ]
)

print(response["message"]["content"])
