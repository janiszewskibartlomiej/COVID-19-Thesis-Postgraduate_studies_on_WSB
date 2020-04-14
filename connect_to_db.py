import sqlite3


class ConnectToDb:

    def __init__(self, db='db.sqlite'):
        self.conn = sqlite3.connect(db)
        # self.conn.row_factory = sqlite3.Row
        self.c = self.conn.cursor()

    def row_factory(self):
        self.conn.row_factory = sqlite3.Row

    def insert_record(self, query, parameters):
        self.c.execute(query, parameters)
        self.conn.commit()

    def select_one_record(self, query, parameter):
        self.c.execute(query, parameter)
        return self.c.fetchone()

    def select_all_record(self, query, parameter):
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
