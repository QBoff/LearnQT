import sqlite3


def get_result(name):
    db = sqlite3.connect(name)
    cur = db.cursor()
    req = '''
    DELETE FROM films
    WHERE genre = (
        SELECT id FROM genres WHERE title = 'фантастика'
    ) AND year < 2000 AND duration > 90
    '''
    cur.execute(req)
    db.commit()
    db.close()
