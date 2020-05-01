# Completed tasks:


## Version 1.0

1. Schema and SQL script
2. Connecting to db and runing sql script > creating db SQLite
    Class with methods:
      - insert records, 
      - select data
      - execute script
      - commit to db
      - closing db
3. Importer of countries data from API json to database: https://restcountries.eu/rest/v2/all
    Class with methods: 
      - load data 
      - insert to db
4. Importer of historical cases from json files or REST API to database: https://api.covid19api.com/all
    Class with methods:
      - read json files or from api
      - load and write json file
      - creating row to insert db
      - load name and id of countries
      - creating dict of countries name and id
      - load all data from json file or rest api and insert to db
5. Importer of current cases from json files or REST API to db: https://api.covid19api.com/summary
    Class with method > load data from json file or rest api  
6. Data processing and creating map of the world with markers and information about current cases by countries
    Class with methods"
      - select all cases per day
      - select current cases
      - get icon color from preparing dict where keys = number of #colors and value = list of interval
      - slice location form string of list
      - creating maps with individual markers, popup with name of country, cases > used html tags
      
7. Flask server to render index.html

## Version 1.1:

 1. Title in map like marker - used DivIcon function, because in folium we haven't got method creating title
 2. Table of total current cases like marker with DivIcon method from API json https://covid19.mathdro.id/api
 3. Class Graphs with elastic methods to fast creating JS graphs [plotly lib] to every country in our database. This class we can use also to api json if we process data in pandas. Simple method processing data from DB to DF we have also.   
 4. Separation of methods in graphs.py because I need more flex methods.
 5. New method -  Join two graphs and run everything from url parameter.
 6. Added button in every popup box, when user click on - run the creating of graph.
 7. Implementing every logic in Flask server.
 
