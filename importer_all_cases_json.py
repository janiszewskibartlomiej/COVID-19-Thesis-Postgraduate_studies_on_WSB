import json
import time
import requests

from path_and_api import *
from importer_of_countries import ImporterOfCountries


class ImporterAllCases(ImporterOfCountries):

    def __init__(self):

        super().__init__()

        self.query_select_cases_id_and_date = "SELECT province, city, confirmed, recovered, deaths FROM cases WHERE country_id = ? " \
                                              "and last_update LIKE ? ;"
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

    def load_name_and_id_of_countries(self):

        query = 'SELECT alpha_2_code, id FROM countries;'
        connect = ImporterAllCases()
        list_of_data = connect.select_all_records(query=query, parameter='')
        connect.close_connect()
        print(f'--> Script {ImporterAllCases.load_name_and_id_of_countries.__name__} executed <--')
        return list_of_data

    def create_dict_of_countries_name_and_id(self, data):

        countries_and_id_dict = {}
        for row in data:
            countries_and_id_dict[row[0]] = row[1]
        print(f'--> Script {ImporterAllCases.create_dict_of_countries_name_and_id.__name__} executed <--')
        return countries_and_id_dict

    def load_all_data_from_json_and_insert_to_db(self, path, api=True):

        time_start = time.time()
        importer = ImporterAllCases()

        if api is True:
            data = importer.read_json_api(path)
        else:
            data = importer.read_json_file(path)

        load_countries = importer.load_name_and_id_of_countries()
        symbol_dict = importer.create_dict_of_countries_name_and_id(load_countries)
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
                parameters = importer.creating_row_to_insert_db(row_dict=row)

                row_cases = (element['Province'], element['City'],
                             element['Confirmed'], element['Recovered'], element['Deaths'])

                verify_duplicate_zero = (element['Province'], element['City'],
                                         0, 0, 0)

                if row_cases != verify_duplicate_zero:
                    importer.insert_record(query=self.query_insert_cases, parameters=parameters)
                    print('Insert record: ', parameters)

            except KeyError:
                if KeyError == 'AN':
                    continue

        print(f'--> Insert cases from json {path} is done <--')
        time_stop = time.time()
        delta = time_stop - time_start
        print('Import time is ', round(delta / 60, 2), ' minutes')
        importer.close_connect()


if __name__ == '__main__':
    importer = ImporterAllCases()

    # importer.load_all_data_from_json_and_insert_to_db(path=JsonApi.API_ALL_CASES)
    # importer.load_all_data_from_json_and_insert_to_db(path='./resources/json/all_data.json', api=False)

    # data = importer.read_json_api(JsonApi.API_ALL_CASES)
    # print('len: ', len(data), '\n', data[0].keys(), '\n', data[0:3], end="")
    x = '2020-04-06T00:00:00Z'
    t = f"'{x[:10]}%'"
    z = "2020-04-18T09:13:50Z"
    db_last_update = importer.select_all_records(query=importer.query_select_cases_id_and_date,
                                                 parameter=(240, z))
    print(db_last_update, type(db_last_update))

    print(("", "", 699148, 58545, 36758) in db_last_update)
