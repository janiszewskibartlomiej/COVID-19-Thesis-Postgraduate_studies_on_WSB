from importer_cases_json import ImporterCases
from map_of_the_world import CreatingMap
from resources.path_and_api import JsonApi

if __name__ == "__main__":
    ImporterCases().load_all_data_from_json_and_insert_to_db(
        path=JsonApi.API_ALL_CASES, api=True, current_cases=True
    )
    CreatingMap().map_of_the_world()
