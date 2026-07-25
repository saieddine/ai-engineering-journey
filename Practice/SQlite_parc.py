import sqlite3
connection= sqlite3.connect('chatboot.db')
cursor=connection.cursor()
cursor.execute("""CREATE TABLE people (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    first_name TEXT,

    last_name TEXT

)""")
connection.commit()
connection.close()

