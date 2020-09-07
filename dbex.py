import sqlite3
conn = sqlite3.connect('testingdb.sqlite')
cur = conn.cursor()
cur.execute('SELECT * FROM Test Where Phone="12345" ')
for row in cur.fetchall():
    print(row)

cur.close()
conn.commit()
conn.close()

