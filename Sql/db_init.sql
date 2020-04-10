PRAGMA foreign_keys = ON;


DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS cases;


CREATE TABLE countries(
  id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  alpha3Code TEXT NOT NULL,
  country_code INTEGER NOT NULL,
  population INTEGER NOT NULL,
  latlng TEXT NOT NULL,
  flag_url TEXT NOT NULL
);

CREATE TABLE cases(
  id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT UNIQUE,
  created_at INTEGER NOT NULL,
  country_id INTEGER NOT NULL UNIQUE,
  confirmed INTEGER,
  recovered INTEGER,
  deaths INTEGER,
  lastUpdate TEXT NOT NULL,
  FOREIGN KEY (country_id) REFERENCES countries (id)
);

