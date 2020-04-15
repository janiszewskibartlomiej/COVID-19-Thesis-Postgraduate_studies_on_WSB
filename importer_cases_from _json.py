import json
import requests
import time
from connect_to_db import ConnectToDb
from path_and_api import *


class ImporterCurrentCases(ConnectToDb):

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

    def load_current_data_from_json_and_insert_to_db(self, path, api=True):

        importer = ImporterCurrentCases()
        if api is True:
            data = importer.read_json_api(path)
        else:
            data = importer.read_json_file(path)

        load_data = importer.load_name_and_id_of_countries()
        symbol_dict = importer.create_dict_of_countries_name_and_id(load_data)
        for element in data['Countries']:
            try:
                coutry_code = element['CountryCode']
                country_id = symbol_dict[coutry_code]
                row = {
                    'timestamp': int(time.time()),
                    'cod2': country_id,
                    'confirmed': element['TotalConfirmed'],
                    'recovery': element['TotalRecovered'],
                    'deaths': element['TotalDeaths'],
                    'last_update': element['Date']
                }
                parameters = row.values()
                parameters = tuple(parameters)
                query_select = "SELECT confirmed, recovered, deaths FROM cases WHERE country_id = ?"
                row_like_select_construction = (
                    element['TotalConfirmed'], element['TotalRecovered'], element['TotalDeaths'])
                query_insert = 'INSERT INTO cases VALUES(null, ?, ?, ?, ?, ?, ?);'

                db_last_update = importer.select_all_record(query=query_select, parameter=(country_id,))
                # print(tuple(db_last_update), row_like_select_construction)
                # print(row_like_select_construction not in tuple(db_last_update))

                if row_like_select_construction not in db_last_update:
                    importer.insert_record(query=query_insert, parameters=parameters)
                    print('Insert record: ', parameters)

            except KeyError:
                if KeyError == 'AN':
                    continue
            except TypeError:
                importer.insert_record(query=query_insert, parameters=parameters)
                print('Insert record: ', parameters)
        print(f'--> Insert cases from json {path} is done <--')
        importer.close_connect()

    def load_name_and_id_of_countries(self):

        query = 'SELECT alpha_2_code, id FROM countries;'
        connect = ConnectToDb()
        list_of_data = connect.select_all_record(query=query, parameter='')
        connect.close_connect()
        print(f'--> Script {ImporterCurrentCases.load_name_and_id_of_countries.__name__} executed <--')
        return list_of_data

    def create_dict_of_countries_name_and_id(self, data):

        countries_and_id_dict = {}
        for row in data:
            countries_and_id_dict[row[0]] = row[1]
        print(f'--> Script {ImporterCurrentCases.create_dict_of_countries_name_and_id.__name__} executed <--')
        return countries_and_id_dict


if __name__ == '__main__':
    importer = ImporterCurrentCases()
    importer.load_data_and_write_json(JsonApi.API_CURRENT_CASES, Files.JSON_CURRENT_DATA)
    importer.load_data_and_write_json(JsonApi.API_HISTORICAL_CASES, Files.JSON_ALL_DATA)

    # importer.load_data_from_json_and_insert_to_db(path=JsonApi.API_CURRENT_CASES)
    # importer.load_data_from_json_and_insert_to_db(path='./resources/json/current_data.json_12', api=False)
