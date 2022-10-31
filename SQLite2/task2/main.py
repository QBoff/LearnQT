import sqlite3


def get_result(name):
    db = sqlite3.connect(name)
    cur = db.cursor()
    req = '''
    UPDATE films
    SET duration = '42'
    WHERE duration = ''
    '''
    cur.execute(req)
    db.commit()
    db.close()
