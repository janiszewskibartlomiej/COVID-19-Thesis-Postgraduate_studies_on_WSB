import json
import requests

API_JSON_CURRENT_CASES = "https://api.covid19api.com/summary"
API_JSON_HISTORICAL_CASES = "https://api.covid19api.com/all"

JSON_ALL_DATA = "./resources/json/all_data_13.json"
JSON_CURRENT_DATA = "./resources/json/current_data_13.json"


def load_data_and_write_json(url, file_name):
    response = requests.get(url)
    data = response.json()
    print(f'--> Success write of "{file_name}"" <--')
    with open(file=file_name, mode='w', encoding='utf-8') as f:
        json.dump(data, f)


if __name__ == '__main__':

    load_data_and_write_json(API_JSON_HISTORICAL_CASES, JSON_ALL_DATA)
    load_data_and_write_json(API_JSON_CURRENT_CASES, JSON_CURRENT_DATA)

