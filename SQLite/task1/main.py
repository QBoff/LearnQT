import sqlite3

name = input()
a = sqlite3.connect(name)
b = a.cursor()
queue = ('''
         SELECT films.title FROM films, 
         genres WHERE films.duration >= 60 AND 
         films.genre = genres.id AND 
         genres.title = "комедия"
         ''')
c = b.execute(queue).fetchall()
for i in c:
    print(i[0])
