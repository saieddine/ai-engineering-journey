class PromptEngineer:
    """
    Builds prompts for the LLM.
    """

    def __init__(self):
        pass

    def build_context(self, retrieved_chunks):
        """
        Convert retrieved chunks into a readable context.
        """

        context = ""

        for index, result in enumerate(retrieved_chunks, start=1):

            page = result["chunk"]["page"]

            text = result["chunk"]["text"]

            context += (
                f"========== Context {index} (Page {page}) ==========\n"
            )

            context += text

            context += "\n\n"

        return context

    def build_prompt(self, question, retrieved_chunks):
        """
        Build the complete prompt for the LLM.
        """

        context = self.build_context(retrieved_chunks)

        prompt = f"""
You are an AI Academic Assistant for Northwestern Polytechnical University (NPU).

Your primary goal is to help students understand their course material.

Instructions:

1. Use the provided course material as your PRIMARY source of information.

2. If the course material is incomplete, you may use your own computer science knowledge to:
   - clarify difficult concepts,
   - provide examples,
   - connect related ideas,
   - make explanations easier to understand.

3. Never contradict the provided course material.

4. If you add information that is not directly found in the course material, integrate it naturally while keeping the course material as the foundation of your explanation.

5. Teach the student instead of simply answering.

------------------------------------------------------------

COURSE MATERIAL

{context}

------------------------------------------------------------

STUDENT QUESTION

{question}

------------------------------------------------------------

Answer:
"""

        return prompt