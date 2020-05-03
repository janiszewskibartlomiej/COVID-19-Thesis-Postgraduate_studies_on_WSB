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
        title = 'COVID-19 Thesis by Bartlomiej Janiszewski & Piotr Woźniak'

        data = self.total_current_cases()

        cases_map = folium.Map(location=[62.0, 20.0], width='99%', height='99%', left='0%', top='0%', zoom_start=3.5,
                               max_zoom=6, min_zoom=3.5, titles=title, attr="attribution")
        folium.map.Marker(
            [70.0, 26.0],
            icon=DivIcon(
                icon_size=(300, 50),
                icon_anchor=(178, 85),
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
                icon_anchor=(227, 40),
                html=f'<div style="background-color:rgba(255, 255, 255, 0.4);">'
                f'<center><h4 style="line-height: 150%";><b>Total cases: </b></h4>'
                f'<h4 style="color: red; line-height: 150%;">Confirmed: <b>{chr(127973)} {total_confirmed}</b></h4>'
                f'<h4 style="color: black;">Deaths: <b> {chr(10015)} {total_deats}</b></h4>'
                f'<h4 style="color: green; line-height: 150%;">Recovered: <b>{chr(128154)} {total_recovered}</b></h4></center>'
                f'<div style=" display: flex; justify-content: space-around">'
                f'<button class="btn btn-primary btn-sm" type="button" style="    padding: 5px 5px;" onclick=window.open("/graphs","_self")>Join two graphs</button> <button class="btn btn-primary btn-sm" type="button" style=" padding: 5px 5px;" onclick=window.open("/graph=0")>World graph</button> </div>'
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
                    popup=folium.Popup(html=f"""<div style="opacity:1.3;">
                    <center><b style="font-size:13px;">{row[1]}</b></center>
                    </br>
                    Confirmed: <b><center><p style="color:red;  font-size:14px; margin-block-start: 0.6em;">{chr(127973)} {confirmed}</p></center></b>
                    Deaths: <b><center><p style="color:black; font-size:14px; margin-block-start: 0.6em;">{chr(10015)} {deaths}</p></center></b>
                    Recovered: <b><center><p style="color:green; font-size:14px; margin-block-start: 0.6em;">{chr(128154)} {recovered}</p></center></b>
                    <center><button type="button" class="btn btn-primary btn-sm" style=" padding: 5px; "line-height: 1;" onclick=window.open("/graph={row[0]}")>Graph</button></center>
                             </div>""", max_width=150),
                    icon=folium.Icon(color='red', icon='certificate', html="position: absolute; z-index: 1"),
                    tooltip=f"""
                    <center>Click me</center>
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
        cases_map.save('index.html')  # only for github


if __name__ == '__main__':
    CreatingMap().map_of_the_world()
