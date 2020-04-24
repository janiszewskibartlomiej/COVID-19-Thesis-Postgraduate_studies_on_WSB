import sys
import folium
from folium import DivIcon
from connect_to_db import ConnectToDb
from importer_all_cases_json import ImporterAllCases
from path_and_api import JsonApi

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

    def total_all_cases_per_day(self):
        data = ConnectToDb().select_all_records(
            self.query_select_sum_of_cases_per_day_group_by_id, "")
        return data

    def total_current_cases(self):
        data = ConnectToDb().select_all_records(self.query_select_sum_of_cases_current_day, "")
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

    def creating_map(self):
        title = 'COVID-19 Thesis made by Piotr Woźniak & Bartlomiej Janiszewski'

        data = DataProcessing().total_current_cases()

        cases_map = folium.Map(location=[62.0, 20.0], width='99%', height='99%', left='0%', top='0%', zoom_start=3.5,
                               max_zoom=6, min_zoom=3, titles=title, attr="attribution")
        folium.map.Marker(
            [70.0, 26.0],
            icon=DivIcon(
                icon_size=(290, 50),
                icon_anchor=(179, 85),
                html=f'<div style="color: #484545; position: absolute; z-index: -1"><h4>{title}</h4></div>',
            )
        ).add_to(cases_map)

        total_data_today = ImporterAllCases().read_json_api(JsonApi.API_TOTAL_TODAY)
        total_confirmed = f"{total_data_today['confirmed']['value']: ,}".replace(',', ' ')
        total_deats = f"{total_data_today['deaths']['value']: ,}".replace(',', ' ')
        total_recovered = f"{total_data_today['recovered']['value']: ,}".replace(',', ' ')

        folium.map.Marker(
            [70.0, 32.0],
            icon=DivIcon(
                icon_size=(210, 180),
                icon_anchor=(220, 30),
                html=f'<div style="background-color:rgba(255, 255, 255, 0.4);">'
                f'<center><h4 style="line-height: 150%";><b>Total cases: </b></h4>'
                f'<h4 style="color: red; line-height: 150%;">Confirmed: <b>{chr(127973)} {total_confirmed}</b></h4>'
                f'<h4 style="color: black;">Deaths: <b> {chr(10015)} {total_deats}</b></h4>'
                f'<h4 style="color: green; line-height: 150%;">Recovered: <b>{chr(128154)} {total_recovered}</b></h4></center>'
                f'</div>',
            )
        ).add_to(cases_map)

        for row in data:
            try:
                coordinates = self.slice_location(row[7])

                confirmed = f'{row[3]: ,}'.replace(',', " ")
                deaths = f'{row[4]: ,}'.replace(',', " ")
                recovered = f'{row[5]: ,}'.replace(',', " ")

                folium.Marker(
                    location=[coordinates[0], coordinates[1]],
                    icon=folium.Icon(color='red', icon='certificate', html="position: absolute; z-index: 1"),
                    tooltip=f"""
                    <center><b>{row[1]}</b></center>
                    </br>
                    Confirmed: <b><center><p style="color:red;">{chr(127973)} {confirmed}</p></center></b>
                    Deaths: <b><center><p style="color:black;">{chr(10015)} {deaths}</p></center></b>
                    Recovered: <b><center><p style="color:green;">{chr(128154)} {recovered}</p></center></b>
                             """
                ).add_to(cases_map)

                color = DataProcessing().get_icon_color(row[3])

                folium.CircleMarker(
                    location=[coordinates[0], coordinates[1]],
                    radius=10,
                    color=f"{color}",
                    fill=True,
                    fill_color=f"{color}"
                ).add_to(cases_map)

            except ValueError:
                continue

        cases_map.save('./templates/index.html')
        cases_map.save('index.html')


if __name__ == '__main__':
    DataProcessing().creating_map()
