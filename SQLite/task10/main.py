import sqlite3


db = sqlite3.connect(input())
cur = db.cursor()

for i in cur.execute(
    '''SELECT title FROM films WHERE title LIKE "%Астерикс%" AND title NOT LIKE "%Обеликс%"'''
):
    print(i[0])

db.close()
