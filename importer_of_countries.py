import json
import sqlite3
from urllib.request import urlopen
from conect_to_db import connect_to_db

API = "https://restcountries.eu/rest/v2/all"


def load_data_from_api(url):
    with urlopen(url) as file:
        response = file.read()
        data_load = json.loads(response)
        print(data_load)
        solution = []
        for item in data_load:
            name = (item['name'])
            alpha3code = (item['alpha3Code'])
            alpha2code = (item['alpha2Code'])
            population = (item['population'])
            latlag = (item['latlng'])
            flag = (item['flag'])
            row = {'name': name,
                   'alpha3code': alpha3code,
                   'alpha2code': alpha2code,
                   'population': population,
                   'latlag': str(latlag),
                   'flag': str(flag)}
            solution.append(row)
        return solution


def insert_data_to_db(data):
    conn = connect_to_db()
    c = conn.cursor()
    for row in data:
        row = (row.values())
        query = 'INSERT INTO countries VALUES(null, "{}", "{}", "{}", {}, "{}", "{}");'.format(*row)
        print(query)
        try:
            c.execute(query)
            conn.commit()
        except sqlite3.IntegrityError:
            continue
    conn.close()
    return print(f'--> Script executed pass <--')


if __name__ == '__main__':
    data_slice = load_data_from_api(API)

    insert_data_to_db(data_slice)
