import sqlite3


def get_result(name):
    db = sqlite3.connect(name)
    cur = db.cursor()
    req = '''
    DELETE FROM films
    WHERE title LIKE 'Я%а'
    '''
    cur.execute(req)
    db.commit()
    db.close()
