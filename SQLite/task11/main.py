import sqlite3


genre = input()
db = sqlite3.connect("music_db.sqlite")
cur = db.cursor()
req = '''SELECT DISTINCT album.title

FROM track

LEFT JOIN genre ON track.genreid = genre.genreid
LEFT JOIN album ON track.albumid = album.albumid
LEFT JOIN artist ON artist.artistid = album.artistid
WHERE genre.name = ?
ORDER BY artist.artistid, album.title;'''

res = cur.execute(req, (genre,))

for i in res:
    print(i[0])

db.close()
