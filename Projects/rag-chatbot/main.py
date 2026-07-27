from app.ingestion.pdf_reader import read_pdf
from app.ingestion.text_cleaner import clean_pages
from app.ingestion.chunker import chunk_pages


pdf_path = "data/pdf/Note 15-05-2026 2(1).pdf"

pages = read_pdf(pdf_path)

cleaned_pages = clean_pages(pages)

chunks = chunk_pages(cleaned_pages)

for chunk in chunks:

    print("=" * 60)

    print(f"Chunk ID : {chunk['chunk_id']}")

    print(f"Page     : {chunk['page']}")

    print()

    print(chunk["text"])

    print()