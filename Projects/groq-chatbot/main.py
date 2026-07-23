from groq import Groq
from dotenv import load_dotenv
import os
import json

# ==============================
# Load environment variables
# ==============================
load_dotenv()

# ==============================
# Create Groq client
# ==============================
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ==============================
# Conversation memory
# ==============================
messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful assistant. "
            "You MUST remember information the user gives you during this conversation "
            "and use it when answering later questions."
        )
    }
]

print("========================================")
print(" Chatbot Started!")
print(" Type 'exit' to quit.")
print("========================================\n")

# ==============================
# Main Chat Loop
# ==============================
while True:

    # --------------------------
    # Get user input
    # --------------------------
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # --------------------------
    # Save user message
    # --------------------------
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # --------------------------
    # Debug: Show memory
    # --------------------------
    print("\n========== MEMORY ==========")
    print(json.dumps(messages, indent=4))
    print("============================\n")

    # --------------------------
    # Send request to Groq
    # --------------------------
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        stream=True,
        temperature=0
    )

    # --------------------------
    # Stream AI response
    # --------------------------
    print("AI: ", end="", flush=True)

    full_response = ""

    for chunk in response:

        if (
            chunk.choices
            and chunk.choices[0].delta
            and chunk.choices[0].delta.content
        ):

            piece = chunk.choices[0].delta.content

            print(piece, end="", flush=True)

            full_response += piece

    print("\n")

    # --------------------------
    # Save assistant response
    # --------------------------
    messages.append(
        {
            "role": "assistant",
            "content": full_response
        }
    )