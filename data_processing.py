import sys
import os
import pandas as pd
from connect_to_db import ConnectToDb

root_path = os.getcwd()
os.chdir(root_path)


class DataProcessing:

    def __init__(self):
        super().__init__()
        self.connection = ConnectToDb()

        self.query_select_sum_of_cases_per_day_group_by_id = """
        SELECT sum(ca.confirmed) as total_confirmed, 
        sum(ca.deaths) as total_deaths, sum(ca.recovered) as total_recovered, 
        max(ca.last_update)
        FROM cases as ca
        JOIN countries as co
        ON ca.country_id = co.country_id
        GROUP BY ca.country_id, ca.last_update
        HAVING ca.country_id = ?
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
        datetime(last_update) as date_of_update
        FROM cases
        GROUP BY datetime(last_update)
        """
        self.interval = {
            '#29a329': [1, 1000],
            '#196619': [1000, 5000],
            '#f2c718': [5000, 10000],
            '#ffcc00': [10000, 25000],
            '#ff9900': [25000, 50000],
            '#ff5c33': [50000, 100000],
            '#ff3300': [100000, 150000],
            '#ff3333': [150000, 250000],
            '#ff0000': [250000, 100 ** 10],
        }

    def all_cases_per_day_where_country_id_equal(self, country_id):
        data = self.connection.select_all_records(query=
                                                  self.query_select_sum_of_cases_per_day_group_by_id,
                                                  parameter=(country_id,))
        return data

    def total_current_cases(self):
        data = self.connection.select_all_records(query=self.query_select_sum_of_cases_current_day, parameter="")
        return data

    def total_cases_per_day(self):
        data = self.connection.select_all_records(query=self.query_select_total_cases_per_day, parameter="")
        return data

    def get_name_and_3code_country(self, country_id):
        select = self.connection.select_one_record(
            query='SELECT name, alpha_3_code from countries WHERE country_id = ?',
            parameter=(country_id,))
        return select

    def get_id_and_name_of_countries(self):
        select = self.connection.select_all_records(
            query='SELECT co.country_id, co.name from countries as co join cases as ca on co.country_id = ca.country_id group by co.country_id having ca.confirmed > 0',
            parameter="")
        return select

    def get_icon_color(self, number_of_cases):
        for key, volume in self.interval.items():
            if volume[1] > number_of_cases >= volume[0]:
                return key

    def slice_location(self, coordinates_str):
        coordinates_str = coordinates_str.replace('[', '')
        coordinates_str = coordinates_str.replace(']', '')
        coordinates_split = coordinates_str.split(',')
        latitude = float(coordinates_split[0])
        longitude = float(coordinates_split[1])
        coordinates = [latitude, longitude]
        return coordinates

    def get_dateframe(self, data):
        dateframe = pd.DataFrame(data, columns=['Confirmed', 'Deaths', 'Recovered', 'Date'])
        return dateframe

    def get_dateframe_diff(self, data):
        df = self.get_dateframe(data=data)
        df_without_date = df.drop(labels='Date', axis=1)
        df_date = df.drop(labels=['Confirmed', 'Deaths', 'Recovered'], axis=1)
        df_diff = df_without_date.diff(axis=0)
        df_diff_with_date = df_diff.join(df_date)
        df_diff_with_date.drop(labels=[0], axis=0)
        return df_diff_with_date

