from data_processing import DataProcessing
from path_and_api import *
from importer_all_cases_json import ImporterAllCases

if __name__ == '__main__':
    run = ImporterAllCases()

    run.run_sql_script(Files.SQL_SCRIPT)

    countries_data = run.load_countries_from_api(JsonApi.API_COUNTRIES)
    run.insert_countries_to_db(countries_data)

    run.load_all_data_from_json_and_insert_to_db(path=JsonApi.API_ALL_CASES, api=True)

    DataProcessing().creating_map()
