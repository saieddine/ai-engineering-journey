from app.ingestion.pdf_reader import read_pdf
from app.ingestion.text_cleaner import clean_pages
from app.ingestion.chunker import chunk_pages
from app.ingestion.embedding_generator import EmbeddingGenerator

from app.retrieval.vector_store import VectorDatabase


def build_database(pdf_path):

    print("\nReading PDF...")

    pages = read_pdf(pdf_path)

    print("Cleaning text...")

    cleaned_pages = clean_pages(pages)

    print("Creating chunks...")

    chunks = chunk_pages(cleaned_pages)

    print(f"Created {len(chunks)} chunks.")

    print("Generating embeddings...")

    generator = EmbeddingGenerator()

    embedded_chunks = generator.generate_embeddings(chunks)

    print("Saving vector database...")

    database = VectorDatabase()

    database.save(embedded_chunks)

    print("\nDatabase created successfully!")

    print(f"Stored {len(embedded_chunks)} chunks.")


if __name__ == "__main__":

    pdf_path = "data/pdf/Note 15-05-2026 2(1).pdf"

    build_database(pdf_path)