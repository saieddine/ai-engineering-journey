# Document Ingestion Pipeline

## Overview

Before an AI system can answer questions about university courses, it must first transform raw documents into structured knowledge.

The purpose of the Document Ingestion Pipeline is to prepare educational material so that it can later be embedded, stored, searched, and retrieved.

---

## Pipeline

PDF

↓

PDF Reader

↓

Text Cleaner

↓

Chunker

↓

Embeddings (Future)

↓

Vector Database (Future)

---

## PDF Reader

Purpose:

Read every page of a PDF while preserving its structure.

Responsibilities:

- Open PDF files
- Read page by page
- Extract text
- Preserve page numbers

Output Example:

```python
{
    "page": 1,
    "text": "..."
}
```

---

## Text Cleaner

Purpose:

Improve the quality of extracted text before further processing.

Responsibilities:

- Remove unnecessary spaces
- Normalize whitespace
- Remove blank lines
- Preserve readable formatting

The cleaner only modifies formatting and never changes the meaning of the content.

---

## Chunker

Purpose:

Divide documents into smaller searchable knowledge units.

Responsibilities:

- Split large documents
- Preserve context
- Assign chunk IDs
- Preserve page information

Current Strategy:

- Split by paragraphs
- Split large paragraphs into smaller chunks

Future Strategy:

- Topic-based chunking
- Heading detection
- Adaptive chunk sizes
- Overlapping chunks

---

## Why Chunking Matters

Large Language Models perform better when they receive only the information relevant to the student's question.

Chunking allows the retrieval system to return only the most useful sections of a document instead of the entire document.

---

## Future Improvements

- OCR correction
- Table extraction
- Image extraction
- AI verification
- Semantic chunking
- Overlapping chunks