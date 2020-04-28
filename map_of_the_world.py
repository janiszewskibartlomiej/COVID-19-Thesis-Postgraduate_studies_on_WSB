import sys
import folium
from folium import DivIcon
from importer_all_cases_json import ImporterAllCases
from path_and_api import JsonApi
from data_processing import DataProcessing

sys.setrecursionlimit(10000)


class CreatingMap(DataProcessing):

    def __init__(self):
        super().__init__()

    def map_of_the_world(self):
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
                if (row[3], row[4], row[5]) == (0, 0, 0):
                    continue

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
        cases_map.save('index.html') #only for github


if __name__ == '__main__':
    CreatingMap().map_of_the_world()
