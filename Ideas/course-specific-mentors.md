# Course-Specific AI Mentors

## Status

Planned

---

## Overview

Instead of one chatbot answering questions from every university subject, the NPU Academic Assistant will provide specialized AI mentors for each course.

Each mentor will use the same Large Language Model but will retrieve knowledge only from its own course materials.

Examples:

- Data Structures Mentor
- Calculus Mentor
- Computer Organization Mentor
- Operating Systems Mentor

---

## Motivation

Students usually ask questions within one specific course.

Restricting retrieval to course-specific knowledge improves:

- Retrieval accuracy
- Response quality
- Speed
- Context relevance

---

## Architecture

Student

↓

Course Selection

↓

Course Knowledge Base

↓

Retriever

↓

Prompt Builder

↓

LLM

↓

Answer

---

## Future Improvements

- Personalized teaching style per course
- Course progress tracking
- Automatic weakness detection
- Course-specific memory