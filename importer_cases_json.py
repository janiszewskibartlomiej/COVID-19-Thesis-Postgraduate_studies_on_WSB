import json
import time
from datetime import date, timedelta
import requests
from connect_to_db import ConnectToDb


class ImporterCases:
    def __init__(self):
        self.connection = ConnectToDb()

        self.query_select_cases_id_and_date = r"""
        SELECT province, city, confirmed, recovered, deaths FROM cases WHERE country_id = ? and last_update LIKE ? ;
        """
        self.query_insert_cases = (
            r"INSERT INTO cases VALUES(null, ?, ?, ?, ?, ?, ?, ?, ?);"
        )

    def creating_row_to_insert_db(self, row_dict):
        parameters = row_dict.values()
        return tuple(parameters)

    def read_json_file(self, path):

        with open(path, mode="r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    def read_json_api(self, api):

        response = requests.get(api)
        time.sleep(5)
        data = response.json()
        return data

    def load_data_and_write_json(self, url, file_name):
        response = requests.get(url)
        data = response.json()
        print(f'--> Success write of "{file_name}"" <--')
        with open(file=file_name, mode="w", encoding="utf-8") as f:
            json.dump(data, f)

    def load_alpha2code_and_id_of_countries(self):

        query = r"SELECT alpha_2_code, country_id FROM countries;"
        list_of_data = self.connection.select_all_records(query=query, parameter="")
        self.connection.close_connect()
        print(
            f"--> Script {ImporterCases.load_alpha2code_and_id_of_countries.__name__} executed <--"
        )
        return list_of_data

    def create_dict_of_countries_name_and_id(self, data):

        countries_and_id_dict = {}
        for row in data:
            countries_and_id_dict[row[0]] = row[1]
        print(
            f"--> Script {ImporterCases.create_dict_of_countries_name_and_id.__name__} executed <--"
        )
        return countries_and_id_dict

    def load_all_data_from_json_and_insert_to_db(
        self, path, api=True, current_cases=True
    ):

        time_start = time.time()

        if api is True:
            data = self.read_json_api(path)
        else:
            data = self.read_json_file(path)

        load_countries = self.load_alpha2code_and_id_of_countries()
        time.sleep(3)
        symbol_dict = self.create_dict_of_countries_name_and_id(load_countries)
        time.sleep(3)

        for element in data:
            try:
                coutry_code = element["CountryCode"]
                country_id = symbol_dict[coutry_code]
                row = {
                    "timestamp": int(time.time()),
                    "cod2": country_id,
                    "province": element["Province"],
                    "city": element["City"],
                    "confirmed": element["Confirmed"],
                    "recovery": element["Recovered"],
                    "deaths": element["Deaths"],
                    "last_update": element["Date"],
                }
                parameters = self.creating_row_to_insert_db(row_dict=row)

                if parameters[2] != "":
                    continue

                if current_cases:
                    date_element = element["Date"][:10]
                    yesterday = date.today() - timedelta(days=1)
                    yesterday_str = yesterday.__str__()
                    if date_element < yesterday_str:
                        continue

                    db_last_update = ConnectToDb().select_all_records(
                        query=self.query_select_cases_id_and_date,
                        parameter=(country_id, yesterday_str + "%"),
                    )
                    if db_last_update:
                        continue

                row_cases = (
                    element["Province"],
                    element["City"],
                    element["Confirmed"],
                    element["Recovered"],
                    element["Deaths"],
                )

                verify_duplicate_zero = (element["Province"], element["City"], 0, 0, 0)

                if row_cases != verify_duplicate_zero:
                    ConnectToDb().insert_record(
                        query=self.query_insert_cases, parameters=parameters
                    )
                    print("Insert record: ", parameters)

            except KeyError:
                if KeyError == "AN":
                    continue

        print(f"--> Insert cases from json {path} is done <--")

        time_stop = time.time()
        delta = time_stop - time_start

        if current_cases:
            print("Import time current cases = ", round(delta / 60, 2), " minutes")
        print("Import time historical cases = ", round(delta / 60, 2), " minutes")

        self.connection.close_connect()
