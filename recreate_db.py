from conect_to_db import connect_to_db


def run_script(scripts):
    conn = connect_to_db()
    c = conn.cursor()
    with open(scripts, mode='r', encoding='utf-8') as file:
        query = file.read()
    c.executescript(query)
    conn.commit()
    conn.close()
    print(f'\n --> Script "{file.name}" executed <--')


if __name__ == '__main__':
    SCRIPT = './sql/db_init.sql'
    run_script(SCRIPT)
