Today I learned how to make a chatbot remember conversations even after it closes.

The problem

Before, the chatbot only stored messages in RAM. RAM is fast, but it is temporary. When the program closes, everything in RAM is deleted. So the chatbot forgets everything every time.

The solution

We use SQLite, a small database file, to save messages permanently. Now the conversation stays even after closing the program.

New classes I built

DatabaseManager – talks directly to SQLite. It opens the connection, creates tables, saves messages, loads messages, and closes the connection.
MemoryManager – keeps messages in RAM while the program runs, and talks to DatabaseManager to save/load them.
main.py – just starts the app, reads input, shows output. It does not touch the database directly.

Separation of Concerns

Each class should do only one job. Before, main.py did everything, which was messy and hard to fix. Now the work is split between three classes, so the code is cleaner and easier to maintain.

Composition

MemoryManager owns a DatabaseManager object:

python
self.database = DatabaseManager()

This means MemoryManager uses DatabaseManager to do its job, but they stay separate classes. This makes the code more reusable and reduces coupling.

How loading old messages works

When the chatbot starts:

Create MemoryManager
Create DatabaseManager
Load old messages from SQLite
Add them after the system prompt
Conversation is restored

Code:

python
previous_messages = self.database.load_messages()
self.messages.extend(previous_messages)

append() vs extend()

This part was important. If I use append(), it adds the whole list as one single item, so I get a list inside a list. But extend() adds each item separately, so I get one flat list. For merging conversation history, extend() is the correct one.

Principles I practiced

Separation of Concerns – one job per class
Composition – one class owns another
Encapsulation – hide internal details
Abstraction – only show what's needed
DRY – use add_message(role, content) instead of writing separate methods for user and assistant messages

What I have now

A chatbot that:

Remembers past conversations
Creates its database automatically
Loads and saves messages automatically
Has clean, modular code