from database import DatabaseManager


class MemoryManager:

    def __init__(self, system_prompt):

        self.system_prompt = system_prompt

        self.database = DatabaseManager()

        # Start with the system prompt
        self.messages = [
            {
                "role": "system",
                "content": self.system_prompt
            }
        ]

        # Load previous conversation from SQLite
        previous_messages = self.database.load_messages()

        # Add previous messages after the system prompt
        self.messages.extend(previous_messages)

    def add_message(self, role, content):

        message = {
            "role": role,
            "content": content
        }

        # Save in RAM
        self.messages.append(message)

        # Save permanently in SQLite
        self.database.save_message(role, content)

    def get_messages(self):

        return self.messages

    def clear(self):

        # Clear RAM
        self.messages = [
            {
                "role": "system",
                "content": self.system_prompt
            }
        ]

        # Clear SQLite
        self.database.clear_messages()

    def close(self):

        self.database.close()