import sqlite3


class DatabaseManager:

    def __init__(self, database_name="chatbot.db"):

        self.database_name = database_name

        self.connection = sqlite3.connect(self.database_name)

        self.cursor = self.connection.cursor()

        self.initialize_database()

    def initialize_database(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                role TEXT NOT NULL,

                content TEXT NOT NULL,

                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP

            )
        """)

        self.connection.commit()

    def save_message(self, role, content):

        self.cursor.execute(
            """
            INSERT INTO messages (role, content)
            VALUES (?, ?)
            """,
            (role, content)
        )

        self.connection.commit()

    def load_messages(self):

        self.cursor.execute("""
            SELECT role, content
            FROM messages
            ORDER BY id ASC
        """)

        rows = self.cursor.fetchall()

        messages = []

        for row in rows:

            messages.append(
                {
                    "role": row[0],
                    "content": row[1]
                }
            )

        return messages

    def clear_messages(self):

        self.cursor.execute("""
            DELETE FROM messages
        """)

        self.connection.commit()

    def close(self):

        self.connection.close()