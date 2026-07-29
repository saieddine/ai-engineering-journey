import json
import os


class VectorDatabase:
    """
    Stores and loads embedded chunks.
    """

    def __init__(self, database_path="data/vectors/database.json"):

        self.database_path = database_path

        os.makedirs(
            os.path.dirname(database_path),
            exist_ok=True
        )

    def save(self, embedded_chunks):
        """
        Save embedded chunks into a JSON file.
        """

        with open(
            self.database_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                embedded_chunks,
                file,
                ensure_ascii=False,
                indent=4
            )

    def load(self):
        """
        Load embedded chunks from the JSON database.
        """

        if not os.path.exists(self.database_path):
            return []

        with open(
            self.database_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)