import sqlite3

conn = sqlite3.connect('test.db')
print("opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (3,'FAITH',23,450000)")
conn.execute("INSERT INTO EMPLOYEES VALUES (4,'WESLEY',23,450000)")
conn.execute("INSERT INTO EMPLOYEES VALUES (5,'JANE',23,450000)")
conn.execute("INSERT INTO EMPLOYEES VALUES (6,' WENDY',23,450000)")
conn.execute("INSERT INTO EMPLOYEES VALUES (7,'MARK',23,450000)")


conn.commit()
print(" records inserted successfully")
conn.close()