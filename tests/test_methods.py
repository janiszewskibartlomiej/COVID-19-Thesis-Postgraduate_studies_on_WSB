import random
from connect_to_db import ConnectToDb


class TestMethods:
    def __init__(self):
        self.connection = ConnectToDb()

    def get_country_id(self):
        query = r"SELECT country_id FROM cases where confirmed > 0 group by country_id"
        data = self.connection.select_all_records(query=query, parameter="")
        list_id = [x[0] for x in data]
        choise = random.choice(list_id)
        return choise

    def get_location(self):
        query = r"SELECT co.latlng FROM countries as co left join cases as ca on co.country_id = ca.country_id where ca.confirmed > 0 group by co.country_id"
        data = self.connection.select_all_records(query=query, parameter="")
        list_id = [x[0] for x in data]
        choise = random.choice(list_id)
        return choise
