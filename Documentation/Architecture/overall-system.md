# Overall System Architecture

## Overview

The NPU Academic Assistant is an AI-powered educational platform designed to help university students study more efficiently by combining Retrieval-Augmented Generation (RAG), personalized memory, and specialized course knowledge.

Rather than functioning as a general chatbot, the system aims to become a collection of academic mentors capable of answering questions based on university lecture materials, past exams, laboratory reports, exercises, and other educational resources.

The overall architecture follows a modular design, where every component has a single responsibility. This makes the system easier to maintain, debug, and extend as new features are added.

---

## High-Level Architecture

Student

↓

Website (Future)

↓

FastAPI Backend

↓

AI Engine

├── Student Memory

├── Retriever

├── Prompt Builder

├── Verification Layer (Future)

└── Large Language Model

↓

Answer

---

## Components

### Website

The website serves as the interface between students and the AI system.

Responsibilities:

- User authentication
- Course selection
- Chat interface
- Progress tracking
- Resource recommendations
- Exam preparation mode

---

### Backend

The backend coordinates all system components.

Responsibilities:

- Receive student requests
- Communicate with databases
- Retrieve course information
- Build prompts
- Return AI responses

---

### Student Memory

Stores long-term information about each student.

Examples:

- Preferred language
- Weak subjects
- Career goals
- Previous conversations
- Learning progress
- Motivation style

The memory system allows the assistant to personalize explanations and recommendations.

---

### Retriever

Responsible for finding the most relevant knowledge related to the student's question.

Instead of searching using keywords, the retriever searches based on semantic similarity.

---

### Prompt Builder

Combines multiple sources into one prompt:

- Student question
- Retrieved course material
- Student memory
- System instructions

The completed prompt is then sent to the language model.

---

### Verification Layer (Future)

One unique feature planned for this project.

Instead of using AI to clean every uploaded document, the Verification Layer will check only the retrieved chunks before they are sent to the language model.

Benefits:

- Lower API costs
- Faster document ingestion
- Higher response quality

---

### Large Language Model

The LLM generates the final response using:

- Student memory
- Retrieved knowledge
- Prompt instructions

The LLM never answers using memory alone. It relies on retrieved educational material whenever possible.

---

## Design Philosophy

The project follows several software engineering principles:

- Separation of Concerns
- Modular Design
- Single Responsibility Principle
- Incremental Development
- Scalability
- Reusability

---

## Long-Term Vision

The long-term goal is to evolve the NPU Academic Assistant from a simple chatbot into a complete educational platform where every course has its own specialized AI mentor while sharing one common language model.