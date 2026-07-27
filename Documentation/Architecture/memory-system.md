# Memory System Architecture

## Overview

The Memory System allows the assistant to remember important information about each student across multiple conversations.

Instead of remembering every message, the system stores only meaningful long-term facts.

---

## Architecture

Student

↓

Conversation

↓

Memory Manager

↓

SQLite Database

↓

Retrieved Memory

↓

Prompt Builder

↓

LLM

---

## Responsibilities

### Memory Manager

Determines whether new information should be stored.

Examples:

- Weak subjects
- Preferred language
- Career goals
- Favorite learning style

---

### Database

Stores structured student information.

The database serves as long-term memory that survives even after the program closes.

---

### Prompt Builder

Retrieves relevant memories before sending the student's question to the language model.

---

## Design Philosophy

The memory system should:

- Store only important facts
- Ignore temporary information
- Reduce unnecessary tokens
- Personalize future conversations

---

## Future Improvements

- Automatic importance detection
- Memory confidence scores
- Memory updates
- Forgetting outdated information