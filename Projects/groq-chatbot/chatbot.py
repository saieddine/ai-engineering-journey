from config import client, MODEL_NAME, TEMPERATURE


class ChatBot:

    def generate_response(self, messages):

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            stream=True,
            temperature=TEMPERATURE
        )

        full_response = ""

        print("AI: ", end="", flush=True)

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

        return full_response