from importer_current_cases_json import ImporterCurrentCases
from map_of_the_world import CreatingMap
from graphs import Graphs
from path_and_api import JsonApi

if __name__ == '__main__':
    ImporterCurrentCases().load_current_data_from_json_and_insert_to_db(path=JsonApi.API_CURRENT_CASES)
    CreatingMap().map_of_the_world()
    Graphs().cases_of_the_world()
    Graphs().cases_of_the_poland()
