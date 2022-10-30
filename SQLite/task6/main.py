import sqlite3


artist_name = input()
db = sqlite3.connect("music_db.sqlite")
cur = db.cursor()
results = cur.execute('''
    SELECT DISTINCT Name FROM Track
    WHERE AlbumId IN (
        SELECT AlbumId FROM Album
            WHERE ArtistId IN (
                SELECT ArtistId FROM Artist
                    WHERE name = ?))
    ORDER BY Name
''', (artist_name,)).fetchall()

for i in results:
    print(i[0])

db.close()
