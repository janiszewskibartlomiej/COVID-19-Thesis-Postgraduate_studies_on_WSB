import os
import sys
import sqlite3

# root_path = os.getcwd()
# os.chdir(root_path)


class ConnectToDb:

    def __init__(self, db='db.sqlite'):
        self.db = db
        self.conn = sqlite3.connect(self.db)
        self.c = self.conn.cursor()

    def run_sql_script(self, scripts):
        with open(scripts, mode='r', encoding='utf-8') as file:
            query = file.read()
            self.execute_script(query=query)
        print(f'\n --> Script "{file.name}" executed <--')

    def row_factory(self):
        self.conn.row_factory = sqlite3.Row

    def insert_record(self, query, parameters):
        self.c.execute(query, parameters)
        self.conn.commit()

    def delete_record(self, query, parameters):
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

    def close_connect(self):
        self.c.close()


if __name__ == '__main__':
    run = ConnectToDb()
    print(
        run.select_all_records(query='SELECT *, max(last_update) FROM cases WHERE country_id = ?', parameter=(179,)))
    # run.run_sql_script(Files.SQL_SCRIPT)
    print(sys.path)
