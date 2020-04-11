import sqlite3


def connect_to_db(db_name='db.sqlite'):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    print('--> Connect to db is done <--')
    return conn


if __name__ == '__main__':
    connect_to_db()
