import sqlite3 as sq


nameOfDb = input()
db = sq.connect(nameOfDb)
cur = db.cursor()

req = '''
SELECT title FROM Films WHERE genre = 4 AND year <= 2000 AND year >= 1995
'''
res = cur.execute(req).fetchall()

for i in res:
    print(i[0])

db.close()