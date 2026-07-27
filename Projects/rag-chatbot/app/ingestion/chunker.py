def split_paragraphs(text):
    """
    Split text into paragraphs.
    """

    paragraphs = text.split("\n\n")

    return paragraphs


def split_large_paragraph(paragraph, max_words=300):
    """
    Split a large paragraph into smaller chunks.
    """

    words = paragraph.split()

    chunks = []

    for i in range(0, len(words), max_words):

        chunk = " ".join(words[i:i + max_words])

        chunks.append(chunk)

    return chunks


def create_chunk(chunk_id, page, text):
    """
    Create one chunk dictionary.
    """

    return {
        "chunk_id": chunk_id,
        "page": page,
        "text": text
    }


def chunk_pages(pages):

    all_chunks = []

    chunk_id = 1

    for page in pages:

        paragraphs = split_paragraphs(page["text"])

        for paragraph in paragraphs:

            paragraph = paragraph.strip()

            if len(paragraph) < 30:
                continue

            small_chunks = split_large_paragraph(paragraph)

            for chunk in small_chunks:

                all_chunks.append(
                    create_chunk(
                        chunk_id,
                        page["page"],
                        chunk
                    )
                )

                chunk_id += 1

    return all_chunks