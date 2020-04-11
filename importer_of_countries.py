import json
import sqlite3
from urllib.request import urlopen
from conect_to_db import connect_to_db

API = "https://restcountries.eu/rest/v2/all"


def load_data_from_api(url):
    with urlopen(url) as file:
        response = file.read()
        data_load = json.loads(response)
        solution = []
        for item in data_load:
            name = (item['name'])
            symbol_of_country = (item['alpha3Code'])
            country_code = (item['numericCode'])
            population = (item['population'])
            latlag = (item['latlng'])
            flag = (item['flag'])
            row = {'name': name,
                   'symbol_of_country': symbol_of_country,
                   'country_code': country_code,
                   'population': population,
                   'latlag': str(latlag),
                   'flag': str(flag)}
            solution.append(row)
        return solution


def insert_data_to_db(data):
    conn = connect_to_db()
    c = conn.cursor()
    for row in data:
        if row['country_code'] == None:
            row['country_code'] = 0
        row = (row.values())
        query = 'INSERT INTO countries VALUES(null, "{}", "{}", {}, {}, "{}", "{}");'.format(*row)
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
