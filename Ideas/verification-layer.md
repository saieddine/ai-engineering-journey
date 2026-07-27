# Verification Layer

## Status

Research Phase

---

## Overview

Instead of using AI to clean every uploaded document during ingestion, the system will verify only the chunks retrieved for the current question.

The retrieved text will be reviewed by the LLM before generating the final answer.

---

## Motivation

Most uploaded documents will never be retrieved.

Running AI over every document would be expensive and unnecessary.

Verifying only retrieved chunks reduces API costs while improving answer quality.

---

## Pipeline

Question

↓

Retriever

↓

Retrieved Chunks

↓

Verification Layer

↓

Prompt Builder

↓

LLM

↓

Answer

---

## Advantages

- Lower API cost
- Better OCR correction
- Better formatting
- Improved answer quality
- Easy to cache corrected chunks

---

## Possible Challenges

- Increased response time
- Risk of changing technical content
- Additional prompt engineering required