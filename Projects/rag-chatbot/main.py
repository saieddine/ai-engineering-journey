import time

from app.ingestion.pdf_reader import read_pdf
from app.ingestion.text_cleaner import clean_pages
from app.ingestion.chunker import chunk_pages
from app.ingestion.embedding_generator import EmbeddingGenerator

from app.retrieval.vector_store import VectorDatabase
from app.retrieval.retriever import Retriever


# ==========================================================
# PDF PATH
# ==========================================================

pdf_path = "data/pdf/Note 15-05-2026 2(1).pdf"


# ==========================================================
# READ PDF
# ==========================================================

pages = read_pdf(pdf_path)


# ==========================================================
# CLEAN TEXT
# ==========================================================

clean_pages_list = clean_pages(pages)


# ==========================================================
# CREATE CHUNKS
# ==========================================================

chunks = chunk_pages(clean_pages_list)

print(f"\nTotal Chunks: {len(chunks)}")


# ==========================================================
# GENERATE EMBEDDINGS
# ==========================================================

start_time = time.perf_counter()

generator = EmbeddingGenerator()

model_loaded_time = time.perf_counter()

embedded_chunks = generator.generate_embeddings(chunks)

finished_time = time.perf_counter()


# ==========================================================
# PERFORMANCE
# ==========================================================

print("\n========== PERFORMANCE ==========")

print(
    f"Model Loading Time      : {model_loaded_time - start_time:.2f} seconds"
)

print(
    f"Embedding Generation    : {finished_time - model_loaded_time:.2f} seconds"
)

print(
    f"Total Time              : {finished_time - start_time:.2f} seconds"
)


# ==========================================================
# SAVE TO VECTOR DATABASE
# ==========================================================

database = VectorDatabase()

database.save(embedded_chunks)

loaded_chunks = database.load()

print("\n========== DATABASE ==========")

print(f"Loaded Chunks : {len(loaded_chunks)}")


# ==========================================================
# FIRST CHUNK
# ==========================================================

first_chunk = loaded_chunks[0]

print("\n========== FIRST CHUNK ==========")

print(f"Chunk ID      : {first_chunk['chunk_id']}")
print(f"Page          : {first_chunk['page']}")
print(f"Text Length   : {len(first_chunk['text'])} characters")
print(f"Vector Length : {len(first_chunk['embedding'])}")

print("\nText Preview:\n")

print(first_chunk["text"][:250])

print("\nFirst 10 Embedding Values:\n")

print(first_chunk["embedding"][:10])


# ==========================================================
# RETRIEVER TEST
# ==========================================================

retriever = Retriever()

results = retriever.retrieve(
    "Explain Booth Multiplication",
    top_k=3
)

print("\n========== RETRIEVER ==========\n")

for index, result in enumerate(results, start=1):

    print(f"Result #{index}")

    print(f"Similarity : {result['similarity']:.4f}")

    print(f"Chunk ID   : {result['chunk']['chunk_id']}")

    print(f"Page       : {result['chunk']['page']}")

    print("\nText:\n")

    print(result["chunk"]["text"][:300])

    print("\n" + "-" * 70)