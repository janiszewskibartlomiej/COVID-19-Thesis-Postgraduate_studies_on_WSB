## Problems and solution of them:

1. Schema - we should know what of column we want use and what kind of date we need.
  - We changed schema a few times because needed some information's and one times we needed to change API 
2. Find good API with good structure to our schema.
  - We chose four API's
3. We connected  four difference API's with difference json structure.
4. Import Big Data - 302 000 records and optimization of loading data.
  - First imports = 480 minutes.
  - We used exceptions because we saw many rows are with 0 value  also duplicate value by province and city versus sum in country- those 'if' method are reduced time import to ~~ 10 minutes.
5.  Loading  about ten thousand rows.
  - We had to change connection with  db to first class - not inheritance class.
6. We found good SQL query's to filter data from three API - we needed many testing.
 - We had duplicate value in the current date.
7. Refactor. 
 - We had to separate some code for new methods.
 - Creating flexible methods.
8. Implementing BE methods to FE and connected them in many library.
 - Used HTML5 and CSS3 to presentation values.
  - Used JS to click action on button - Creating graph.
  - Catching functionality from  url parameters and run method  of presentation graphs
  - Implementing every logic in Flask server.
 9. Folium library have limit about added header and some of information on map.
  - We added information like open popup and used HTML and CSS. 
10. Counting diff between rows:
 - In SQL is not easy to do. I decided use Pandas methods and generate dateframe with solution of count
 - We must change logic about importing current data
11. API bugs:
 - same of value is duplicate and I saw in my graphs anomalies in data .
 - a few rows have counting cases and these rows should delete
