import sqlite3


name = input()
db = sqlite3.connect(name)
cur = db.cursor()

res = cur.execute('''
SELECT DISTINCT title FROM genres
WHERE id IN (
    SELECT genre FROM films WHERE year = 2010 OR year = 2011
)
''').fetchall()

for i in res:
    print(i[0])

db.close()
