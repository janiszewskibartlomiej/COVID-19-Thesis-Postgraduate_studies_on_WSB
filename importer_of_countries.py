import json
import sqlite3
from urllib.request import urlopen
from connect_to_db import ConnectToDb
from path_and_api import *


class ImporterOfCountries(ConnectToDb):

    def load_countries_from_api(self, url):
        with urlopen(url) as file:
            response = file.read()
            data_load = json.loads(response)
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
            print(f'--> Script {ImporterOfCountries.load_countries_from_api.__name__} executed <--')
            return solution

    def insert_countries_to_db(self, data):
        conn = ConnectToDb()
        for row in data:
            parameters = row.values()
            parameters = tuple(parameters)
            query = 'INSERT INTO countries VALUES(null, ?, ?, ?, ?, ?, ?);'
            try:
                conn.insert_record(query=query, parameters=parameters)
                print('Insert record: ', parameters)
            except sqlite3.IntegrityError:
                continue
        conn.close_connect()
        return print(f'--> Script {ImporterOfCountries.insert_countries_to_db.__name__} executed <--')


if __name__ == '__main__':
    importer = ImporterOfCountries()
    # data = importer.load_countries_from_api(url=JsonApi.API_COUNTRIES)
    # importer.insert_countries_to_db(data=data)
