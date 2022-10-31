import sqlite3


def get_result(name):
    db = sqlite3.connect(name)
    cur = db.cursor()
    req = '''
    UPDATE films
    SET duration = 100
    WHERE genre = (
        SELECT id FROM genres WHERE title = 'мюзикл'
    ) AND duration > 100
    '''
    cur.execute(req)
    db.commit()
    db.close()
