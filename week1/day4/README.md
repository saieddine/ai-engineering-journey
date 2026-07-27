1. Introduction

Today marks a transition from learning programming concepts to learning AI Systems Engineering.

Instead of asking:

"How do I code this?"

We now ask:

"How should an intelligent AI system think before answering?"

The goal of AI Engineering is not simply to connect an LLM to an application. The goal is to build an intelligent system that decides:

What information is important.
Where that information should be stored.
When it should be retrieved.
How it should be used to generate the best possible answer.
2. Context Window
Definition

A Context Window is the maximum amount of information an LLM can process in a single request.

An LLM cannot remember unlimited conversations.

Every request has a limit.

Current Problem

Our chatbot currently sends:

System Prompt

↓

Every User Message

↓

Every AI Message

every single time.

After weeks or months, this becomes:

Thousands of Messages

Problems:

Slower responses.
Higher API costs.
Eventually exceeds the model's context limit.
Why Context Management Matters

A good AI system should not send every previous conversation.

Instead, it should decide:

What information is still useful.
What can be removed.
What should be stored permanently.
3. Tokens
Definition

LLMs do not count words.

They count tokens.

A token is a small piece of text determined by the tokenizer.

Long conversations generate many tokens, making requests slower and more expensive.

4. Memory Strategies

During today's discussion, we explored several professional approaches.

Strategy 1 – Sliding Window

Keep only the most recent messages.

Advantages:

Fast.
Cheap.
Easy to implement.

Disadvantages:

AI forgets older conversations.
Strategy 2 – Conversation Summarization

Replace old conversations with a summary.

Example:

Instead of storing:

100 messages about databases

Store:

Earlier discussion covered:

• SQLite
• Relationships
• Persistent Memory

Advantages:

Saves tokens.
Preserves important information.
Strategy 3 – Important Facts Memory

Instead of storing conversations, store important facts.

Example:

Name

Major

University

Career Goal

Weak Subjects

Projects

Advantages:

Very efficient.
Personalizes answers.
Low token usage.
Strategy 4 – Retrieval (RAG)

Instead of remembering everything,

Search only the information related to the user's current question.

Example:

Student asks about Graph Theory.

Retrieve:

Graph Theory lecture
Graph Theory exercises
Graph Theory exam questions

Only those are sent to the LLM.

5. Long-Term Student Memory

Instead of storing only messages, our AI assistant should build a student profile.

Possible long-term memory:

Identity
Name
Student ID
Major
Nationality
Native Language
Academic Profile
Current Courses
Weak Courses
Strong Courses
Current Year
Student Type (International / Chinese)
Learning Preferences
Preferred Learning Style
Motivation
Demotivation
Hobbies
Long-Term Goals
Career Goal
Current Projects
Study Abroad Goal
Progress
Completed Courses
Completed Challenges
Weak Topics
Strong Topics
6. Confidence-Based Memory (Project Idea)

One of today's most important design ideas.

Instead of immediately storing everything,

the AI should assign a confidence level.

Example:

Student says:

"Calculus is difficult."

Confidence

20%

A week later:

"I'm still struggling with Calculus."

Confidence

60%

Later:

"Can you explain derivatives again?"

Confidence

95%

Now the system stores:

Weak Subject

Calculus

This prevents storing temporary or unimportant information while allowing the AI to learn naturally over time.

7. Knowledge Graph Concept

Traditional databases store records.

Example:

Name	Major
Saif	Computer Science

A Knowledge Graph stores relationships.

Example:

Saif

├── Studies → Computer Science

├── Wants → Germany

├── Building → NPU Assistant

├── Weak At → Calculus

└── Enjoys → Basketball

This allows the AI to understand connections instead of isolated facts.

8. Choosing the Right Storage

Different information requires different storage technologies.

SQL Database

Best for:

Students
Courses
Accounts
Structured information
Graph Database

Best for:

Relationships
Learning paths
Course dependencies
Student connections
Vector Database

Best for:

PDFs
Lecture slides
Books
Semantic Search
Engineering Principle

We concluded that:

The goal is not to use more tools.

Instead:

Each tool should solve the problem it is best suited for.

This follows the same engineering principle we learned when separating our chatbot into main.py, MemoryManager, and DatabaseManager.

9. AI Decision Pipeline

One of the most important lessons of today.

An LLM should not immediately answer a question.

Instead, the system should first decide what information the LLM needs.

Pipeline:

Student Question

↓

Intent Detection

↓

Retrieve Student Memory

↓

Retrieve Course Material

↓

Retrieve Past Exams

↓

Retrieve Progress Information

↓

Build Prompt

↓

LLM

↓

Final Personalized Answer

The LLM becomes a reasoning engine.

The surrounding system becomes responsible for providing the correct context.

10. Personalized Learning

Two students may ask the exact same question:

"How should I prepare for my Calculus final?"

The AI should not provide identical answers.

Instead, it should consider:

Weak topics.
Exam date.
Available study time.
Learning preferences.
Previous progress.
Past exam patterns.

Only then should the LLM generate the study plan.

11. Our Vision for the NPU Academic Assistant

During today's discussion, we realized that we are no longer designing a simple chatbot.

We are designing an AI Academic Mentor.

The system should:

Understand each student.
Learn from long-term interactions.
Personalize recommendations.
Recommend learning resources.
Create study plans.
Recommend future courses.
Adapt to exams.
Improve over time.

The AI should feel like a mentor rather than a search engine.

12. Design Ideas Generated Today

During today's brainstorming session, we proposed several ideas that should become future project features.

Confidence-Based Memory

Store information only after sufficient evidence has been observed.

Adaptive Student Profile

Instead of asking many personal questions, the AI should gradually learn about the student through natural conversations.

Memory Categories

Separate memory into:

Identity
Academic Profile
Learning Preferences
Long-Term Goals
Academic Progress
Temporary Conversation Memory
Student Knowledge Graph

Represent students using relationships instead of isolated database records.

13. Key Takeaways
LLMs cannot remember unlimited conversations.
Context management is one of the biggest challenges in AI Engineering.
Important information should be stored separately from conversations.
Different storage technologies solve different problems.
The surrounding system should decide what information the LLM receives.
Good AI systems personalize answers using memory, knowledge retrieval, and reasoning.
Our long-term goal is to build an AI Academic Mentor, not just a chatbot.
Personal Reflection

Today's lesson changed the way I think about AI systems.

I realized that building an intelligent assistant is not only about using an LLM. The real intelligence comes from designing the architecture around it: deciding what to remember, what to retrieve, and how to personalize responses.

One idea that stood out to me was Confidence-Based Memory. Instead of storing every piece of information immediately, the assistant can gradually build confidence by observing repeated patterns or consistent behavior. This makes the system more natural and reduces incorrect assumptions.

I also understood that modern AI systems are composed of multiple specialized components—SQL databases, graph databases, vector databases, memory systems, retrieval pipelines, and the LLM itself. Each component has a clear responsibility, following the same engineering principles we have been applying throughout this journey.

Finally, I no longer see the NPU Academic Assistant as a chatbot. I now see it as an AI Academic Mentor whose goal is to understand each student, adapt to their learning needs, and guide them throughout their university journey. I believe this vision will shape every technical decision we make from now on.