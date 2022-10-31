import sqlite3


def get_result(name):
    db = sqlite3.connect(name)
    cur = db.cursor()
    req = '''
    DELETE FROM films
    WHERE films.genre = (
        SELECT genres.id FROM genres WHERE genres.title = "комедия"
    )
    '''
    cur.execute(req)
    db.commit()
    db.close()
