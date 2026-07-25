from groq import Groq
from dotenv import load_dotenv
from memory import MemoryManager

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
# System Prompt
# ==============================
system_prompt = (
    "You are a helpful assistant. "
    "You MUST remember information the user gives you during this conversation "
    "and use it when answering later questions."
)

# ==============================
# Memory Manager
# ==============================
memory = MemoryManager(system_prompt)

print("========================================")
print(" Chatbot Started!")
print(" Type 'exit' to quit.")
print("========================================\n")

# ==============================
# Main Chat Loop
# ==============================
while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        memory.close()
        print("Goodbye!")
        break

    # --------------------------
    # Save User Message
    # --------------------------
    memory.add_message("user", user_input)

    # --------------------------
    # Debug: Show Memory
    # --------------------------
    print("\n========== MEMORY ==========")
    print(json.dumps(memory.get_messages(), indent=4))
    print("============================\n")

    # --------------------------
    # Send Request to Groq
    # --------------------------
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=memory.get_messages(),
        stream=True,
        temperature=0
    )

    # --------------------------
    # Stream AI Response
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

    print()

    # --------------------------
    # Save Assistant Message
    # --------------------------
    memory.add_message("assistant", full_response)