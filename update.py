import sqlite3

conn = sqlite3.connect('test.db')
print("opened database successfully")

conn.execute("UPDATE EMPLOYEES SET AGE = 67 WHERE ID = 6")
conn.commit()

cursor = conn.execute("SELECT ID,NAME,AGE FROM EMPLOYEES")

for row in cursor:
    print("ID", row[0])
    print("NAME", row[1])
    print("AGE", row[2])
    print("SALARY", row[3])

print("records found")
conn.close()