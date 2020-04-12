import json
import requests
from datetime import date

from conect_to_db import connect_to_db

API_JSON_CURRENT_CASES = "https://api.covid19api.com/summary"
API_JSON_HISTORICAL_CASES = "https://api.covid19api.com/all"


def load_data_and_write_json(url, file_name):
    response = requests.get(url)
    data = response.json()
    with open(file=file_name, mode='w', encoding='utf-8') as f:
        json.dump(data, f)


def load_name_and_id_of_countries():
    conn = connect_to_db()
    c = conn.cursor()
    query = 'SELECT name, id FROM countries;'
    c.execute(query)
    list_of_data = c.fetchall()
    c.close()
    print('--> load name and id <--')
    return list_of_data


def create_dict_of_countries_name_and_id(data):
    countries_and_id_dict = {}
    for row in data:
        countries_and_id_dict[row[3]] = row[1]
    print('--> create dict of countries name and id <--')
    return countries_and_id_dict


if __name__ == '__main__':
    load_data = load_name_and_id_of_countries()
    symbol_dict = create_dict_of_countries_name_and_id(load_data)
    print(symbol_dict)

    ALL_DATA = "./resources/json/all_data.json"
    CURRENT_DATA = "./resources/json/current_data.json"

    load_data_and_write_json(API_JSON_HISTORICAL_CASES, ALL_DATA)
    load_data_and_write_json(API_JSON_CURRENT_CASES, CURRENT_DATA)
