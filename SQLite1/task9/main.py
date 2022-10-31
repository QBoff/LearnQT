import sqlite3


db = sqlite3.connect(input())
cur = db.cursor()

for i in cur.execute(
    "SELECT title FROM films WHERE duration <= 85"
):
    print(i[0])

db.close()
