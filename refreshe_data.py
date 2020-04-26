from importer_current_cases_json import ImporterCurrentCases
from map_of_the_world import CreatingMap
from data_processing import DataProcessing
from graphs import DataGraph
from app import app
from path_and_api import JsonApi

if __name__ == '__main__':
    ImporterCurrentCases().load_current_data_from_json_and_insert_to_db(path=JsonApi.API_CURRENT_CASES)
    CreatingMap().map_of_the_world()
    dataframe = DataProcessing().creating_dateframe(data=DataProcessing().total_cases_per_day())
    DataGraph().creating_graph(dataframe=dataframe, title_of_graph='Cases of the World', country_id=False)
    app.run(debug=True)
