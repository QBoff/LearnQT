import sqlite3


def get_result(name):
    db = sqlite3.connect(name)
    cur = db.cursor()
    req = '''
    UPDATE films
    SET duration = duration * 2
    WHERE genre = (
        SELECT id FROM genres
        WHERE title = "фантастика"
    )
    '''
    cur.execute(req)
    db.commit()
    db.close()
