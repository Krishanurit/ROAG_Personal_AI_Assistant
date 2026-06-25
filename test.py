from ollama import chat

messages = [
    {
        "role": "system",
        "content": "You are ROAG, a personal AI assistant."
    }
]

while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    messages.append(
        {
            "role": "user",
            "content": user
        }
    )

    response = chat(
        model="qwen3:8b",
        messages=messages
    )

    answer = response["message"]["content"]

    print("ROAG:", answer)

    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )