from app.retrieval.retriever import Retriever
from app.chatbot.prompt_engineer import PromptEngineer
from app.chatbot.llm import LLM


retriever = Retriever()

prompt_engineer = PromptEngineer()

llm = LLM()


print("=" * 60)
print("NPU Academic Assistant")
print("=" * 60)


while True:

    question = input("\nYou: ")

    if question.lower() in ["exit", "quit"]:

        print("\nGoodbye!")

        break

    retrieved_chunks = retriever.retrieve(
        question,
        top_k=3
    )

    prompt = prompt_engineer.build_prompt(
        question,
        retrieved_chunks
    )

    answer = llm.generate(prompt)

    print("\nAssistant:\n")

    print(answer)