import sys
from connect_to_db import ConnectToDb

sys.setrecursionlimit(10000)


class DataProcessing(ConnectToDb):

    def __init__(self):
        super().__init__()

        self.query_select_sum_of_cases_per_day_group_by_id = """
        SELECT ca.country_id, co.name, co.alpha_3_code, sum(ca.confirmed) as total_confirmed, 
        sum(ca.deaths) as total_deaths, sum(ca.recovered) as total_recovered, 
        ca.last_update, co.latlng, co.flag_url
        FROM cases as ca
        JOIN countries as co
        ON co.country_id = ca.country_id
        GROUP BY ca.country_id, ca.last_update
        HAVING max(ca.last_update)
        """

        self.query_select_sum_of_cases_current_day = """
        SELECT ca.country_id, co.name, co.alpha_3_code, ca.confirmed as total_confirmed, ca.deaths as total_deaths, 
        ca.recovered as total_recovered, max(ca.last_update), co.latlng, co.flag_url
        FROM cases as ca
        JOIN countries as co
        ON co.country_id = ca.country_id
        GROUP BY ca.country_id
        """

        self.query_select_total_cases_per_day = """
        SELECT sum(confirmed) as total_confirmed, sum(deaths) as total_deaths, sum(recovered) as total_recovered, 
        date(last_update) as date_of_update
        FROM cases
        GROUP BY date(last_update)
        """
        self.interval = {
            '#29a329': [1, 1000],
            '#196619': [1000, 5000],
            '#f2c718': [1000, 10000],
            '#ffcc00': [10000, 25000],
            '#ff9900': [25000, 50000],
            '#ff5c33': [50000, 100000],
            '#ff3300': [100000, 150000],
            '#ff3333': [150000, 250000],
            '#ff0000': [250000, 100 ** 10],
        }

    def all_cases_per_day_and_country(self):
        data = ConnectToDb().select_all_records(
            self.query_select_sum_of_cases_per_day_group_by_id, "")
        return data

    def total_current_cases(self):
        data = ConnectToDb().select_all_records(self.query_select_sum_of_cases_current_day, "")
        return data

    def total_cases_per_day(self):
        data = ConnectToDb().select_all_records(self.query_select_total_cases_per_day, "")
        return data

    def get_icon_color(self, number_of_cases):
        for key, volume in self.interval.items():
            if volume[1] > number_of_cases >= volume[0]:
                return key

    def slice_location(self, coordinates_str):
        coordinates_str = coordinates_str.replace('[', '')
        coordinates_str = coordinates_str.replace(']', '')
        coordinates = coordinates_str.split(',')
        latitude = float(coordinates[0])
        longitude = float(coordinates[1])
        coordinates = [latitude, longitude]
        return coordinates
