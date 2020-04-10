import json
from urllib.request import urlopen

API = "https://restcountries.eu/rest/v2/all"


def load_data_from_api(url):
    with urlopen(url) as file:
        response = file.read()
        data_load = json.loads(response)
        solution = []
        for item in data_load:
            name = (item['name'])
            symbol_of_country = (item['alpha3Code'])
            country_code = (item['numericCode'])
            population = (item['population'])
            latlag = (item['latlng'])
            flag = (item['flag'])
            row = {'name': name,
                   'symbol_of_country': symbol_of_country,
                   'country_code': country_code,
                   'population': population,
                   'latlag': latlag,
                   'flag': flag}
            solution.append(row)
        return solution


if __name__ == '__main__':
    data_slice = load_data_from_api(API)
    print(data_slice)
