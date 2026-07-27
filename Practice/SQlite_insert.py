import sqlite3
connection=sqlite3.connect("chatbot.db")
cursor=connection.cursor()
many_students=[
    (2020, 'BESSAM', 'SAIF'),
    (22, 'Ghit', 'sott'),
    (23, 'LATIF', 'SLAM')
]
cursor.executemany(" INSERT INTO students VALUES(?,?,?)", many_students)
connection.commit()
connection.close()