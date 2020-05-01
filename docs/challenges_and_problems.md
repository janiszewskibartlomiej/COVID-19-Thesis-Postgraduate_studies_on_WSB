## Problems and solution of them:

1. Schema - we should know what of column we want use and what kind of date we need.
  - We changed schema a few times because needed some information's and one times we needed to change API 
2. Find good API with good structure to our schema.
  - We chose four API's
3. We connected  four difference API's with difference json structure.
4. Import Big Data - 302 000 records and optimization of loading data.
  - First imports = 480 minutes.
  - We used exceptions because we saw many rows are with 0 value - those 'if' method are reduced time import to ~~ 80 minutes.
5.  Loading  about ten thousand rows - in core python  we have default limit five thousand.
  - We found solution and changed to 10 000.
  - We had to change connection with  db to first class - not inheritance class.
6. We found good SQL query's to filter data from three API - we needed many testing.
 - We had duplicate value in the current date.
7. Refactor. 
 - We had to separate some code for new methods.
 - Creating flexible methods.
