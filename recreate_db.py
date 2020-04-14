from conect_to_db import ConnectToDb
from path_and_api import *


def run_script(scripts):
    conn = ConnectToDb()
    with open(scripts, mode='r', encoding='utf-8') as file:
        query = file.read()
        conn.execute_script(query=query)
    print(f'\n --> Script "{file.name}" executed <--')


if __name__ == '__main__':
    run_script(Files.SCRIPT)
