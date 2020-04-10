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
            iso = (item['alpha3Code'])
            country_code = (item['numericCode'])
            population = (item['population'])
            latlag = (item['latlng'])
            flag = (item['flag'])
            row = [name, iso, country_code, population, latlag, flag]
            solution.append(row)
        return solution


if __name__ == '__main__':
    data_slice = load_data_from_api(API)
    print(data_slice)
