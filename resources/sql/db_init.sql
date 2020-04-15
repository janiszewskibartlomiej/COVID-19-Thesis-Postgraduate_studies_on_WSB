PRAGMA foreign_keys = ON;


DROP TABLE IF EXISTS cases;
DROP TABLE IF EXISTS countries;


CREATE TABLE countries(
  id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  alpha_3_code TEXT UNIQUE NOT NULL,
  alpha_2_code TEXT UNIQUE NOT NULL,
  population INTEGER NOT NULL,
  latlng TEXT UNIQUE NOT NULL,
  flag_url TEXT UNIQUE NOT NULL
);

CREATE TABLE cases(
  id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT UNIQUE,
  created_at INTEGER NOT NULL,
  country_id INTEGER NOT NULL,
  confirmed INTEGER,
  recovered INTEGER,
  deaths INTEGER,
  last_update TEXT NOT NULL,
  FOREIGN KEY (country_id) REFERENCES countries (id)
);
