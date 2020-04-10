import sqlite3


def run_script(scripts, db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    with open(scripts, mode='r', encoding='utf-8') as file:
        query = file.read()
    c.executescript(query)
    conn.commit()
    conn.close()

    print(f'Script "{file.name}" executed pass')


if __name__ == '__main__':
    DATABASE_NAME = 'db.sqlite'
    SCRIPT = './sql/db_init.sql'
    run_script(SCRIPT, DATABASE_NAME)
