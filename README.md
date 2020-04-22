# COVID-19-Thesis-Postgraduate_studies_on_WSB ![alt text](https://poplawski.legal/wp-content/uploads/2017/08/Tydzie%C5%84-Mediacji-WSB-Adwokat-Szczecin-Adam-Pop%C5%82awski.jpg "Logo WSB")
------------------------------------

#### Project COVID-19 > completed tasks:  ![alt text](https://s3.amazonaws.com/ae-lane-report/wp-content/uploads/2020/03/16140821/Document.jpeg "COVID_19")

1. Schema and SQL script
2. Connect to db and runer sql script > creating db SQLite
    Class with methods:
      - insert recors, 
      - select data
      - execute script
      - commit to db
      - close db
3. Creating importer countries data from API json to database: https://restcountries.eu/rest/v2/all
    Class with methods: 
      - load data 
      - insert to db
4. Creating class importer historical cases from json files or REST API to database: https://api.covid19api.com/all
    Class with methods:
      - read json files or from api
      - load and write json file
      - creating row to insert db
      - load name and id of countries
      - creating dict of countries name and id
      - load all data from json file or rest api and insert to db
5. Creating importer current cases from json files or REST API to db: https://api.covid19api.com/summary
    Class with method > load data from json file or rest api  
6. Data processing and creating map of the world with markers and information about curren cases by coutries
    Class with methods"
      - select all cases per day
      - select current cases
      - get icon color from prepering dict where keys = number of #colors and valume = list of interval
      - slice location form string of list
      - creating maps with inywidual markers, popup with name of coutry, cases > used html tags
7. Flask server to render incese index.html

#### Start instructions:

1. `clone` `repo`
2. `pip install -r requirements.txt`
3. `creating_app.py`
4. `app.py`
