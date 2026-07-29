from sentence_transformers import SentenceTransformer


class EmbeddingGenerator:
    """
    Generates vector embeddings using SentenceTransformers.
    """

    def __init__(self, model_name="all-MiniLM-L6-v2"):
        """
        Load the embedding model.
        """
        self.model = SentenceTransformer(model_name)

    def generate_embedding(self, text):
        """
        Generate an embedding for a single piece of text.

        Args:
            text (str): Input text.

        Returns:
            list: Embedding vector.
        """

        embedding = self.model.encode(
            text,
            convert_to_numpy=True
        )

        return embedding.tolist()

    def generate_embeddings(self, chunks):
        """
        Generate embeddings for all chunks using batch processing.

        Args:
            chunks (list): List of chunk dictionaries.

        Returns:
            list: Chunks with embeddings added.
        """

        texts = [chunk["text"] for chunk in chunks]

        embeddings = self.model.encode(
            texts,
            batch_size=32,
            convert_to_numpy=True,
            show_progress_bar=True
        )

        embedded_chunks = []

        for chunk, embedding in zip(chunks, embeddings):

            embedded_chunk = chunk.copy()

            embedded_chunk["embedding"] = embedding.tolist()

            embedded_chunks.append(embedded_chunk)

        return embedded_chunks