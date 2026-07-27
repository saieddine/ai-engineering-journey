# Retrieval System Architecture

## Overview

The Retrieval System is responsible for finding the most relevant knowledge before the language model generates an answer.

Rather than searching using keywords, the system compares semantic meaning using embeddings.

---

## Planned Pipeline

Student Question

↓

Embedding Model

↓

Question Vector

↓

Vector Database

↓

Top Relevant Chunks

↓

Verification Layer (Future)

↓

Prompt Builder

↓

LLM

↓

Answer

---

## Components

### Embedding Model

Converts text into numerical vectors representing semantic meaning.

---

### Vector Database

Stores embeddings generated from course materials.

Examples:

- Lecture slides
- Past exams
- Laboratory reports
- Books
- Exercises

---

### Retriever

Searches for chunks whose embeddings are closest to the student's question.

---

### Verification Layer

Verifies retrieved chunks before sending them to the language model.

This feature aims to improve answer quality while keeping operating costs low.

---

## Long-Term Goal

Support specialized retrieval for every university course while using one central language model.