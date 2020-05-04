import time
from connect_to_db import ConnectToDb
from importer_all_cases_json import ImporterAllCases
from resources.path_and_api import JsonApi


class ImporterCurrentCases(ImporterAllCases):

    def __init__(self):

        super().__init__()

    def load_current_data_from_json_and_insert_to_db(self, path, api=True):

        if api is True:
            data = self.read_json_api(path)
        else:
            data = self.read_json_file(path)

        load_data = self.load_name_and_id_of_countries()
        symbol_dict = self.create_dict_of_countries_name_and_id(load_data)

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

                parameters = self.creating_row_to_insert_db(row_dict=row)

                row_like_select_construction = ("", "",
                                                element['TotalConfirmed'], element['TotalRecovered'],
                                                element['TotalDeaths'])
                if row_like_select_construction == ("", "", 0, 0, 0):
                    continue

                date_element = element['Date'][:10]
                db_last_update = ConnectToDb().select_all_records(query=self.query_select_cases_id_and_date,
                                                                  parameter=(country_id, date_element + '%'))

                if row_like_select_construction not in db_last_update or db_last_update == []:
                    ConnectToDb().insert_record(query=self.query_insert_cases, parameters=parameters)
                    print('Insert record: ', parameters)

            except KeyError:
                if KeyError == 'AN':
                    continue
        print(f'--> Insert cases from json {path} is done <--')
        self.close_connect()


if __name__ == '__main__':
    ImporterCurrentCases().load_current_data_from_json_and_insert_to_db(JsonApi.API_CURRENT_CASES)

    db_last_update = ConnectToDb().select_all_records(query=ImporterCurrentCases().query_select_cases_id_and_date,
                                                      parameter=(179, '2020-05-04' + '%'))
    print(db_last_update)