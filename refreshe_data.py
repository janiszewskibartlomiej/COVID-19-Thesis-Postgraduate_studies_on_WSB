from importer_current_cases_json import ImporterCurrentCases
from data_processing import DataProcessing
from app import app
from path_and_api import JsonApi

if __name__ == '__main__':
    ImporterCurrentCases().load_current_data_from_json_and_insert_to_db(path=JsonApi.API_CURRENT_CASES)
    DataProcessing().creating_map()
    app.run(debug=True)
