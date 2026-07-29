from sentence_transformers.util import cos_sim

from app.ingestion.embedding_generator import EmbeddingGenerator
from app.retrieval.vector_store import VectorDatabase


class Retriever:

    def __init__(self):

        self.embedding_generator = EmbeddingGenerator()

        self.database = VectorDatabase()

    def retrieve(self, question, top_k=3):

        question_embedding = self.embedding_generator.generate_embedding(question)

        database = self.database.load()

        scored_chunks = []

        for chunk in database:

            similarity = cos_sim(
                question_embedding,
                chunk["embedding"]
            ).item()

            scored_chunks.append(
                {
                    "similarity": similarity,
                    "chunk": chunk
                }
            )

        scored_chunks.sort(
            key=lambda x: x["similarity"],
            reverse=True
        )

        return scored_chunks[:top_k]