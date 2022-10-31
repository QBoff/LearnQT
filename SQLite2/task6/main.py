import sqlite3


def get_result(name):
    db = sqlite3.connect(name)
    cur = db.cursor()
    req = '''
    DELETE FROM films
    WHERE duration >= 90 AND genre = (
        SELECT id FROM genres
        WHERE title = "боевик"
    )
    '''
    cur.execute(req)
    db.commit()
    db.close()
