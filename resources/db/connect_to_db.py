import pathlib
import sqlite3
from path_and_api import Files
class ConnectToDb:

    def __init__(self):
        db_path = pathlib.Path('db.sqlite').absolute()
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()

    def run_sql_script(self, scripts):
        conn = ConnectToDb()
        with open(scripts, mode='r', encoding='utf-8') as file:
            query = file.read()
            conn.execute_script(query=query)
        print(f'\n --> Script "{file.name}" executed <--')

    def row_factory(self):
        self.conn.row_factory = sqlite3.Row

    def insert_record(self, query, parameters):
        self.c.execute(query, parameters)
        self.conn.commit()

    def select_one_record(self, query, parameter):
        self.c.execute(query, parameter)
        return self.c.fetchone()

    def select_all_records(self, query, parameter):
        self.c.execute(query, parameter)
        return self.c.fetchall()

    def execute_script(self, query):
        self.conn.executescript(query)
        self.conn.commit()
        self.c.close()

    def commit(self):
        self.conn.commit()

    def close_connect(self):
        self.c.close()


if __name__ == '__main__':
    run = ConnectToDb()
    print(run.select_one_record(query='SELECT * FROM cases WHERE country_id = ?', parameter=(179, )))
    # run.run_sql_script(Files.SQL_SCRIPT)
