import sqlite3
connection= sqlite3.connect('chatbot.db')
cursor=connection.cursor()
cursor.execute("SELECT * FROM students")
items=cursor.fetchall()
print(f"{'ID':<8}{'First Name':<15}{'Last Name'}")
print("-" * 33)
for item in items:(
    print(f"{item[0]:<8}{item[1]:<15}{item[2]}")
)
connection.commit()
connection.close()