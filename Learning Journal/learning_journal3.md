Learning Journal — Week 2

Date: (Fill in the date)

Week 2 — From Learning AI to Designing AI Systems

This week marked a major turning point in my AI Engineering journey. During the previous weeks, I focused on understanding the theoretical concepts behind Large Language Models (LLMs), memory systems, databases, Retrieval-Augmented Generation (RAG), and how AI applications are structured. This week was different. Instead of only learning concepts, I started building the first production components of the NPU Academic Assistant.

The first component I completed was the PDF Reader. Using PyMuPDF, I learned how to open a PDF document, extract text page by page, and organize the extracted information into a structured format. Rather than treating the document as one long string, I stored every page as a dictionary containing its page number and text. This helped me understand an important software engineering principle: preserving structure makes later processing much easier.

After building the reader, I developed the Text Cleaner. At first, I thought the cleaner would simply remove unnecessary spaces. However, I realized that its real purpose is to prepare documents for the entire AI pipeline. I separated the cleaning process into several small functions, each responsible for one task, such as normalizing whitespace, removing extra spaces, removing unnecessary blank lines, and trimming leading and trailing spaces. This reinforced another engineering principle that I have been seeing repeatedly: every module should have one clear responsibility.

One important discussion this week was about using AI to clean documents. My first instinct was to let an LLM correct every document immediately after extraction. After thinking more carefully about scalability, I proposed a different idea. Instead of cleaning every document with AI, the system should only verify the chunks that are actually retrieved when a student asks a question. This would significantly reduce API costs because only information that students use would be verified. We also discussed caching the corrected version so that future students would benefit without requiring another AI verification. I believe this Verification Layer may become one of the unique features of our project.

Another major topic this week was chunking. Initially, I thought splitting documents into fixed-size pieces would be enough. After discussing how students actually ask questions, I concluded that documents should be divided by topics whenever possible because students search for concepts rather than page numbers. At the same time, I realized that a topic can sometimes become too large, which reduces retrieval quality. The solution we designed was to split large topics into smaller chunks while keeping each chunk focused on one complete idea. This taught me that the ideal chunk is neither too small nor too large—it should contain one complete idea without mixing unrelated concepts.

I also started thinking more like a system architect instead of simply writing code. Throughout the week, I noticed that many of my questions changed from "How do I implement this?" to "How should this system be designed?" We discussed metadata, specialized knowledge bases, document processing pipelines, memory systems, and how every component should communicate with the others. This shift in thinking has been one of the most valuable lessons of the week.

One idea that I became increasingly confident about is organizing the NPU Academic Assistant around specialized academic mentors. Instead of having one generic chatbot that knows every subject, I want each course to have its own knowledge base while sharing the same language model. This architecture should improve retrieval accuracy, make the system easier to expand, and create a more personalized learning experience for students.

By the end of Week 2, I successfully completed the first version of the document ingestion pipeline:

PDF
   ↓
PDF Reader
   ↓
Text Cleaner
   ↓
Chunker

Although this pipeline is simple, it forms the foundation of the entire RAG system. Every future component—embeddings, vector databases, retrieval, prompt construction, and AI responses—will depend on it.

Challenges I Faced
Understanding how to organize a professional Python project.
Fixing import errors after restructuring the project folders.
Learning how Python packages work using __init__.py.
Designing modules instead of writing everything inside one file.
Deciding how to split documents into meaningful chunks.
Engineering Lessons
A module should have one responsibility.
Build Version 1 before designing Version 10.
Clean data before processing it.
Preserve structure throughout the pipeline.
Good architecture makes future improvements much easier.
Retrieval quality depends heavily on chunk quality.
Metadata is almost as important as the text itself.
AI should be used where it adds value, not where simple rules already solve the problem.
My Contributions This Week
Proposed adding a Verification Layer that checks retrieved chunks with an LLM instead of cleaning every document during ingestion.
Suggested organizing the assistant into specialized course mentors sharing one central language model.
Chose topic-based chunking while recognizing the need to split overly large topics.
Emphasized maintaining a modular project structure so every component has a clear responsibility.
Goals for Week 3
Learn how embeddings represent document meaning.
Build the embedding generation pipeline.
Learn how vector databases store semantic information.
Build the retrieval system.
Begin connecting retrieval with the LLM to answer questions from course materials.
My Reflection

This week felt like the moment I stopped thinking of AI as "calling an API" and started thinking about it as a complete software system. Every new module I built made me realize that successful AI products are not created by one powerful model alone, but by many carefully designed components working together. The NPU Academic Assistant is beginning to feel like a real engineering project rather than just a learning exercise, and I can already see how the architectural decisions we make now will influence the system months from today.