import time
from map_of_the_world import CreatingMap
from resources.path_and_api import JsonApi, Files
from importer_all_cases_json import ImporterAllCases
from importer_current_cases_json import ImporterCurrentCases

if __name__ == '__main__':
    run = ImporterAllCases()

    run.run_sql_script(Files.SQL_SCRIPT)

    countries_data = run.load_countries_from_api(JsonApi.API_COUNTRIES)
    run.insert_countries_to_db(countries_data)

    run.load_all_data_from_json_and_insert_to_db(path=JsonApi.API_ALL_CASES, api=True)
    time.sleep(7)
    ImporterCurrentCases().load_current_data_from_json_and_insert_to_db(path=JsonApi.API_CURRENT_CASES, api=True)

    CreatingMap().map_of_the_world()
