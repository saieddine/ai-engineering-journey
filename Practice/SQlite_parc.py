import sqlite3
connection= sqlite3.connect('chatboot.db')
cursor=connection.cursor()
cursor.execute("""CREATE TABLE poeple (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    ID_number         INTEGER,
    first_name text,
    last_name text

)""")
connection.commit()
connection.close()

