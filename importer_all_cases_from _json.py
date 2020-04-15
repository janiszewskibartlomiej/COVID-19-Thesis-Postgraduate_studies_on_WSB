import time

from path_and_api import *
from importer_current_cases_json import ImporterCurrentCases


class ImporterAllCases(ImporterCurrentCases):

    def load_all_data_from_json_and_insert_to_db(self, path, api=True):

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
                    'confirmed': element['Confirmed'],
                    'recovery': element['Recovered'],
                    'deaths': element['Deaths'],
                    'last_update': element['Date']
                }
                parameters = row.values()
                parameters = tuple(parameters)

                query_select = "SELECT confirmed, recovered, deaths FROM cases WHERE country_id = ?"

                row_like_select_construction = (
                    element['Confirmed'], element['Recovered'], element['Deaths'])

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


if __name__ == '__main__':
    importer = ImporterAllCases()

    importer.load_all_data_from_json_and_insert_to_db(path=JsonApi.API_HISTORICAL_CASES)
    # importer.load_all_data_from_json_and_insert_to_db(path='./resources/json/all_data.json', api=False)

    # data = importer.read_json_api(JsonApi.API_HISTORICAL_CASES)
    # print('len: ', len(data), '\n', data[0].keys(), '\n', data[0:3], end="")
