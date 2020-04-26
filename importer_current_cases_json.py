import time

from importer_all_cases_json import ImporterAllCases
from path_and_api import *


class ImporterCurrentCases(ImporterAllCases):

    def __init__(self):

        super().__init__()

    def load_current_data_from_json_and_insert_to_db(self, path, api=True):

        imp = ImporterCurrentCases()

        if api is True:
            data = imp.read_json_api(path)
        else:
            data = imp.read_json_file(path)

        load_data = imp.load_name_and_id_of_countries()
        symbol_dict = imp.create_dict_of_countries_name_and_id(load_data)

        for element in data['Countries']:
            try:
                coutry_code = element['CountryCode']
                country_id = symbol_dict[coutry_code]

                row = {
                    'timestamp': int(time.time()),
                    'cod2': country_id,
                    'province': "",
                    'city': "",
                    'confirmed': element['TotalConfirmed'],
                    'recovery': element['TotalRecovered'],
                    'deaths': element['TotalDeaths'],
                    'last_update': element['Date']
                }

                parameters = imp.creating_row_to_insert_db(row_dict=row)

                row_like_select_construction = ("", "",
                                                element['TotalConfirmed'], element['TotalRecovered'],
                                                element['TotalDeaths'], element['Date'][:10])

                db_last_update = imp.select_all_records(query=imp.query_select_cases_id_and_date,
                                                        parameter=(country_id, element['Date'][:10]))
                if row_like_select_construction not in db_last_update or db_last_update == []:
                    imp.insert_record(query=imp.query_insert_cases, parameters=parameters)
                    print('Insert record: ', parameters)

            except KeyError:
                if KeyError == 'AN':
                    continue
        print(f'--> Insert cases from json {path} is done <--')
        imp.close_connect()


if __name__ == '__main__':
    ImporterCurrentCases().load_current_data_from_json_and_insert_to_db(JsonApi.API_CURRENT_CASES)
