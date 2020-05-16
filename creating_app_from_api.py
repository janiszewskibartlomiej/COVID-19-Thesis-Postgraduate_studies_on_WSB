import time

from app import app
from connect_to_db import ConnectToDb
from importer_cases_json import ImporterCases
from importer_of_countries import ImporterOfCountries
from map_of_the_world import CreatingMap
from resources.path_and_api import JsonApi, Files

if __name__ == "__main__":
    ConnectToDb().run_sql_script(Files.SQL_SCRIPT)

    countries_data = ImporterOfCountries().load_countries_from_api(
        JsonApi.API_COUNTRIES
    )
    ImporterOfCountries().insert_countries_to_db(countries_data)
    time.sleep(3)
    ImporterCases().load_all_data_from_json_and_insert_to_db(
        path=JsonApi.API_ALL_CASES, api=True, current_cases=False
    )
    time.sleep(3)
    CreatingMap().map_of_the_world()
