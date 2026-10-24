import ollama

from .rag import search_knowledge


def generate_answer(question):

    # Search agriculture knowledge
    results = search_knowledge(question)

    # Combine retrieved information
    context = "\n\n".join(results)

    # Create prompt for Llama
    prompt = f"""
You are an AI Agriculture Assistant helping farmers.

Use the agriculture information below to answer the farmer's question.

Agriculture Information:
{context}

Farmer's Question:
{question}

Instructions:
- Give a clear and simple answer.
- Use only the provided agriculture information when possible.
- Do not invent specific fertilizer doses or pesticide doses.
- If the information is insufficient, say that more information is needed.
- Keep the answer practical and easy to understand.
"""

    # Ask Llama 3.2
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]

# Start terminal chatbot only when this file is run directly
if __name__ == "__main__":

    while True:

        question = input("\nFarmer: ")

        if question.lower() == "exit":
            print("Goodbye!")
            break

        answer = generate_answer(question)

        print("\nAI Agriculture Assistant:")
        print(answer)