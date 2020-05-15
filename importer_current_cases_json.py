import time
from connect_to_db import ConnectToDb
from importer_all_cases_json import ImporterAllCases


class ImporterCurrentCases:

    def __init__(self):

        self.connection = ConnectToDb()
        self.all_cases = ImporterAllCases()

    def load_current_data_from_json_and_insert_to_db(self, path, api=True):

        if api is True:
            data = self.all_cases.read_json_api(path)
        else:
            data = self.all_cases.read_json_file(path)

        load_data = self.all_cases.load_alpha2code_and_id_of_countries()
        time.sleep(3)
        symbol_dict = self.all_cases.create_dict_of_countries_name_and_id(load_data)
        time.sleep(3)

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

                parameters = self.all_cases.creating_row_to_insert_db(row_dict=row)

                row_like_select_construction = ("", "",
                                                element['TotalConfirmed'], element['TotalRecovered'],
                                                element['TotalDeaths'])
                if row_like_select_construction == ("", "", 0, 0, 0):
                    continue

                date_element = element['Date'][:10]
                db_last_update = self.connection.select_all_records(query=self.all_cases.query_select_cases_id_and_date,
                                                                    parameter=(country_id, date_element + '%'))

                if db_last_update:
                    self.connection.delete_record(
                        query='DELETE FROM cases WHERE country_id = ? and last_update LIKE ?;',
                        parameters=(country_id, date_element + '%'))

                ConnectToDb().insert_record(query=self.all_cases.query_insert_cases, parameters=parameters)
                print('Insert record: ', parameters)

            except KeyError:
                if KeyError == 'AN':
                    continue
        print(f'--> Insert cases from json {path} is done <--')
        self.connection.close_connect()
