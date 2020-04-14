import json
import time
from connect_to_db import connect_to_db

JSON_ALL_DATA = "./resources/json/all_data.json"
JSON_CURRENT_DATA = "./resources/json/current_data.json"


def load_data_from_json_file_and_insert_to_db(path):
    with open(path, mode='r', encoding='utf-8') as f:
        data = json.load(f)
        load_data = load_name_and_id_of_countries()
        symbol_dict = create_dict_of_countries_name_and_id(load_data)
        conn = connect_to_db()
        c = conn.cursor()
        # print(len(data))
        # print(data.keys())
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
                row_like_select_construction = (element['TotalConfirmed'], element['TotalRecovered'], element['TotalDeaths'])
                query_select = f"SELECT confirmed, recovered, deaths FROM cases WHERE country_id = {country_id}"
                c.execute(query_select)
                db_last_update = c.fetchone()
                if db_last_update[0:] == row_like_select_construction:
                    break

                row = (row.values())
                query_insert = 'INSERT INTO cases VALUES(null, {}, {}, {}, {}, {}, "{}");'.format(*row)
                c.execute(query_insert)
                conn.commit()
                print(query_insert)
            except KeyError:
                if KeyError == 'AN':
                    continue
            except TypeError:
                row = (row.values())
                query_insert = 'INSERT INTO cases VALUES(null, {}, {}, {}, {}, {}, "{}");'.format(*row)
                c.execute(query_insert)
                conn.commit()
                print(query_insert)
        print(f'--> Insert cases from json file {path} is done <--')
        c.close()


def load_name_and_id_of_countries():
    conn = connect_to_db()
    c = conn.cursor()
    query = 'SELECT alpha_2_code, id FROM countries;'
    c.execute(query)
    list_of_data = c.fetchall()
    c.close()
    print('--> load name and id <--')
    return list_of_data


def create_dict_of_countries_name_and_id(data):
    countries_and_id_dict = {}
    for row in data:
        countries_and_id_dict[row[0]] = row[1]
    print('--> create dict of countries name and id <--')
    return countries_and_id_dict


if __name__ == '__main__':
    load_data_from_json_file_and_insert_to_db(JSON_CURRENT_DATA)
