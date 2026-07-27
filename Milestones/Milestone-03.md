# Milestone 03 — Document Ingestion Pipeline

**Date: 27/07/2026

---

# Overview

This milestone marks the completion of the first complete subsystem of the NPU Academic Assistant.

The focus of this milestone was building the **Document Ingestion Pipeline**, which transforms raw PDF documents into structured, searchable chunks that will later be stored inside a vector database.

Although no AI model is answering questions yet, this milestone provides the foundation upon which the entire Retrieval-Augmented Generation (RAG) system will be built.

---

# Objectives

- Build a PDF Reader
- Build a Text Cleaner
- Build a Chunking System
- Create a modular project structure
- Prepare the data for embeddings

---

# Completed Components

## PDF Reader

Responsibilities:

- Open PDF documents
- Read every page
- Extract text
- Preserve page numbers
- Return structured page objects

Output Structure

```python
{
    "page": 1,
    "text": "..."
}
```

---

## Text Cleaner

Responsibilities:

- Normalize whitespace
- Remove unnecessary spaces
- Remove blank lines
- Clean extracted text
- Preserve page information

This module prepares documents before chunking.

---

## Chunker

Responsibilities:

- Split cleaned text
- Preserve context
- Create searchable chunks
- Assign unique chunk IDs

Output Structure

```python
{
    "chunk_id": 1,
    "page": 3,
    "text": "..."
}
```

---

# Final Pipeline

PDF

↓

PDF Reader

↓

Text Cleaner

↓

Chunker

---

# Engineering Principles Applied

- Separation of Concerns
- Single Responsibility Principle
- Modular Design
- Reusable Components
- Incremental Development

---

# Design Decisions

### Topic-Based Chunking

Students search for concepts rather than pages.

Large topics will later be divided into smaller chunks.

---

### Rule-Based Cleaning

Rule-based cleaning is fast, deterministic, and free.

AI verification will be added later.

---

### Metadata Preservation

Every chunk keeps important metadata such as page numbers to improve traceability.

---

### Future Verification Layer

Instead of sending every document to an LLM during ingestion, the system will verify only the retrieved chunks before generating answers.

This reduces API costs while improving retrieval quality.

---

# Technologies Used

- Python
- PyMuPDF
- Regular Expressions (re)

---

# Lessons Learned

Building an AI system is not simply calling an LLM API.

The quality of the answers depends heavily on the quality of the document pipeline.

Every stage in the pipeline has a single responsibility, making the system easier to maintain, extend, and debug.

---

# Future Improvements

- OCR correction
- Heading detection
- Semantic chunking
- Adaptive chunk sizes
- Overlapping chunks
- Table extraction
- Image extraction
- AI verification layer

---

# Milestone Status

✅ Completed