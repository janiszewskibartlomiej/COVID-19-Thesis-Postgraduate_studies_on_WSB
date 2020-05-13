import json
import time
import requests
from resources.path_and_api import JsonApi
from connect_to_db import ConnectToDb


class ImporterAllCases:

    def __init__(self):
        self.connection = ConnectToDb()

        self.query_select_cases_id_and_date = """
        SELECT province, city, confirmed, recovered, deaths FROM cases WHERE country_id = ? and last_update LIKE ? ;
        """
        self.query_insert_cases = 'INSERT INTO cases VALUES(null, ?, ?, ?, ?, ?, ?, ?, ?);'

    def creating_row_to_insert_db(self, row_dict):
        parameters = row_dict.values()
        return tuple(parameters)

    def read_json_file(self, path):

        with open(path, mode='r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def read_json_api(self, api):

        response = requests.get(api)
        data = response.json()
        return data

    def load_data_and_write_json(self, url, file_name):
        response = requests.get(url)
        data = response.json()
        print(f'--> Success write of "{file_name}"" <--')
        with open(file=file_name, mode='w', encoding='utf-8') as f:
            json.dump(data, f)

    def load_alpha2code_and_id_of_countries(self):

        query = 'SELECT alpha_2_code, country_id FROM countries;'
        list_of_data = self.connection.select_all_records(query=query, parameter='')
        self.connection.close_connect()
        print(f'--> Script {ImporterAllCases.load_alpha2code_and_id_of_countries.__name__} executed <--')
        return list_of_data

    def create_dict_of_countries_name_and_id(self, data):

        countries_and_id_dict = {}
        for row in data:
            countries_and_id_dict[row[0]] = row[1]
        print(f'--> Script {ImporterAllCases.create_dict_of_countries_name_and_id.__name__} executed <--')
        return countries_and_id_dict

    def load_all_data_from_json_and_insert_to_db(self, path, api=True):

        time_start = time.time()

        if api is True:
            data = self.read_json_api(path)
        else:
            data = self.read_json_file(path)

        load_countries = self.load_alpha2code_and_id_of_countries()
        symbol_dict = self.create_dict_of_countries_name_and_id(load_countries)
        for element in data:
            try:
                coutry_code = element['CountryCode']
                country_id = symbol_dict[coutry_code]
                row = {
                    'timestamp': int(time.time()),
                    'cod2': country_id,
                    'province': element['Province'],
                    'city': element['City'],
                    'confirmed': element['Confirmed'],
                    'recovery': element['Recovered'],
                    'deaths': element['Deaths'],
                    'last_update': element['Date']
                }
                parameters = self.creating_row_to_insert_db(row_dict=row)

                row_cases = (element['Province'], element['City'],
                             element['Confirmed'], element['Recovered'], element['Deaths'])

                verify_duplicate_zero = (element['Province'], element['City'],
                                         0, 0, 0)

                if row_cases != verify_duplicate_zero:
                    self.connection.insert_record(query=self.query_insert_cases, parameters=parameters)
                    print('Insert record: ', parameters)

            except KeyError:
                if KeyError == 'AN':
                    continue

        print(f'--> Insert cases from json {path} is done <--')
        time_stop = time.time()
        delta = time_stop - time_start
        print('Import time is ', round(delta / 60, 2), ' minutes')
        self.connection.close_connect()
