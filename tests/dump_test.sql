PRAGMA foreign_keys = ON;


DROP TABLE IF EXISTS cases;
DROP TABLE IF EXISTS countries;


CREATE TABLE countries(
  country_id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  alpha_3_code TEXT UNIQUE NOT NULL,
  alpha_2_code TEXT UNIQUE NOT NULL,
  population INTEGER NOT NULL,
  latlng TEXT UNIQUE NOT NULL,
  flag_url TEXT UNIQUE NOT NULL
);
INSERT INTO countries VALUES(62,'Czech Republic','CZE','CZ',10558524,'[49.75, 15.5]','https://restcountries.eu/data/cze.svg');
INSERT INTO countries VALUES(85,'Germany','DEU','DE',81770900,'[51.0, 9.0]','https://restcountries.eu/data/deu.svg');
INSERT INTO countries VALUES(130,'Lithuania','LTU','LT',2872294,'[56.0, 24.0]','https://restcountries.eu/data/ltu.svg');
INSERT INTO countries VALUES(179,'Poland','POL','PL',38437239,'[52.0, 20.0]','https://restcountries.eu/data/pol.svg');

create TABLE cases(
  id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT UNIQUE,
  created_at INTEGER NOT NULL,
  country_id INTEGER NOT NULL,
  province TEXT DEFAULT NULL,
  city TEXT DEFAULT NULL,
  confirmed INTEGER,
  recovered INTEGER,
  deaths INTEGER,
  last_update TEXT NOT NULL,
  FOREIGN KEY (country_id) REFERENCES countries (country_id)
);

INSERT INTO cases VALUES(7226,1588590632,62,'','',3,0,0,'2020-03-01T00:00:00Z');
INSERT INTO cases VALUES(7227,1588590632,62,'','',3,0,0,'2020-03-02T00:00:00Z');
INSERT INTO cases VALUES(7228,1588590632,62,'','',5,0,0,'2020-03-03T00:00:00Z');
INSERT INTO cases VALUES(7229,1588590632,62,'','',8,0,0,'2020-03-04T00:00:00Z');
INSERT INTO cases VALUES(7230,1588590632,62,'','',12,0,0,'2020-03-05T00:00:00Z');
INSERT INTO cases VALUES(7231,1588590632,62,'','',18,0,0,'2020-03-06T00:00:00Z');
INSERT INTO cases VALUES(7232,1588590632,62,'','',19,0,0,'2020-03-07T00:00:00Z');
INSERT INTO cases VALUES(7233,1588590632,62,'','',31,0,0,'2020-03-08T00:00:00Z');
INSERT INTO cases VALUES(7234,1588590632,62,'','',31,0,0,'2020-03-09T00:00:00Z');
INSERT INTO cases VALUES(7235,1588590632,62,'','',41,0,0,'2020-03-10T00:00:00Z');
INSERT INTO cases VALUES(7236,1588590632,62,'','',91,0,0,'2020-03-11T00:00:00Z');
INSERT INTO cases VALUES(7237,1588590632,62,'','',94,0,0,'2020-03-12T00:00:00Z');
INSERT INTO cases VALUES(7238,1588590633,62,'','',141,0,0,'2020-03-13T00:00:00Z');
INSERT INTO cases VALUES(7239,1588590633,62,'','',189,0,0,'2020-03-14T00:00:00Z');
INSERT INTO cases VALUES(7240,1588590633,62,'','',253,0,0,'2020-03-15T00:00:00Z');
INSERT INTO cases VALUES(7241,1588590633,62,'','',298,3,0,'2020-03-16T00:00:00Z');
INSERT INTO cases VALUES(7242,1588590633,62,'','',396,3,0,'2020-03-17T00:00:00Z');
INSERT INTO cases VALUES(7243,1588590633,62,'','',464,3,0,'2020-03-18T00:00:00Z');
INSERT INTO cases VALUES(7244,1588590633,62,'','',694,3,0,'2020-03-19T00:00:00Z');
INSERT INTO cases VALUES(7245,1588590633,62,'','',833,4,0,'2020-03-20T00:00:00Z');
INSERT INTO cases VALUES(7246,1588590633,62,'','',995,6,0,'2020-03-21T00:00:00Z');
INSERT INTO cases VALUES(7247,1588590633,62,'','',1120,6,1,'2020-03-22T00:00:00Z');
INSERT INTO cases VALUES(7248,1588590633,62,'','',1236,6,1,'2020-03-23T00:00:00Z');
INSERT INTO cases VALUES(7249,1588590633,62,'','',1394,10,3,'2020-03-24T00:00:00Z');
INSERT INTO cases VALUES(7250,1588590633,62,'','',1654,10,6,'2020-03-25T00:00:00Z');
INSERT INTO cases VALUES(7251,1588590633,62,'','',1925,10,9,'2020-03-26T00:00:00Z');
INSERT INTO cases VALUES(7252,1588590633,62,'','',2279,11,9,'2020-03-27T00:00:00Z');
INSERT INTO cases VALUES(7253,1588590633,62,'','',2631,11,11,'2020-03-28T00:00:00Z');
INSERT INTO cases VALUES(7254,1588590633,62,'','',2817,11,16,'2020-03-29T00:00:00Z');
INSERT INTO cases VALUES(7255,1588590633,62,'','',3001,25,23,'2020-03-30T00:00:00Z');
INSERT INTO cases VALUES(7256,1588590633,62,'','',3308,45,31,'2020-03-31T00:00:00Z');
INSERT INTO cases VALUES(7257,1588590633,62,'','',3508,61,39,'2020-04-01T00:00:00Z');
INSERT INTO cases VALUES(7258,1588590633,62,'','',3858,67,44,'2020-04-02T00:00:00Z');
INSERT INTO cases VALUES(7259,1588590633,62,'','',4091,72,53,'2020-04-03T00:00:00Z');
INSERT INTO cases VALUES(7260,1588590633,62,'','',4472,78,59,'2020-04-04T00:00:00Z');
INSERT INTO cases VALUES(7261,1588590633,62,'','',4587,96,67,'2020-04-05T00:00:00Z');
INSERT INTO cases VALUES(7262,1588590633,62,'','',4822,121,78,'2020-04-06T00:00:00Z');
INSERT INTO cases VALUES(7263,1588590633,62,'','',5017,172,88,'2020-04-07T00:00:00Z');
INSERT INTO cases VALUES(7264,1588590634,62,'','',5312,233,99,'2020-04-08T00:00:00Z');
INSERT INTO cases VALUES(7265,1588590634,62,'','',5569,301,112,'2020-04-09T00:00:00Z');
INSERT INTO cases VALUES(7266,1588590634,62,'','',5732,346,119,'2020-04-10T00:00:00Z');
INSERT INTO cases VALUES(7267,1588590634,62,'','',5831,411,129,'2020-04-11T00:00:00Z');
INSERT INTO cases VALUES(7268,1588590634,62,'','',5991,464,138,'2020-04-12T00:00:00Z');
INSERT INTO cases VALUES(7269,1588590634,62,'','',6059,519,143,'2020-04-13T00:00:00Z');
INSERT INTO cases VALUES(7270,1588590634,62,'','',6111,642,161,'2020-04-14T00:00:00Z');
INSERT INTO cases VALUES(7271,1588590634,62,'','',6216,819,166,'2020-04-15T00:00:00Z');
INSERT INTO cases VALUES(7272,1588590634,62,'','',6433,972,169,'2020-04-16T00:00:00Z');
INSERT INTO cases VALUES(7273,1588590634,62,'','',6549,1174,173,'2020-04-17T00:00:00Z');
INSERT INTO cases VALUES(7274,1588590634,62,'','',6606,1227,181,'2020-04-18T00:00:00Z');
INSERT INTO cases VALUES(7275,1588590634,62,'','',6746,1298,186,'2020-04-19T00:00:00Z');
INSERT INTO cases VALUES(7276,1588590634,62,'','',6900,1559,194,'2020-04-20T00:00:00Z');
INSERT INTO cases VALUES(7277,1588590634,62,'','',7033,1753,201,'2020-04-21T00:00:00Z');
INSERT INTO cases VALUES(7278,1588590634,62,'','',7132,1989,208,'2020-04-22T00:00:00Z');
INSERT INTO cases VALUES(7279,1588590634,62,'','',7187,2152,210,'2020-04-23T00:00:00Z');
INSERT INTO cases VALUES(7280,1588590634,62,'','',7273,2371,214,'2020-04-24T00:00:00Z');
INSERT INTO cases VALUES(7281,1588590634,62,'','',7352,2453,218,'2020-04-25T00:00:00Z');
INSERT INTO cases VALUES(7282,1588590634,62,'','',7404,2545,220,'2020-04-26T00:00:00Z');
INSERT INTO cases VALUES(7283,1588590634,62,'','',7445,2826,223,'2020-04-27T00:00:00Z');
INSERT INTO cases VALUES(7284,1588590634,62,'','',7504,2948,227,'2020-04-28T00:00:00Z');
INSERT INTO cases VALUES(7285,1588590634,62,'','',7579,3108,227,'2020-04-29T00:00:00Z');
INSERT INTO cases VALUES(7286,1588590634,62,'','',7682,3314,236,'2020-04-30T00:00:00Z');
INSERT INTO cases VALUES(7287,1588590634,62,'','',7737,3372,240,'2020-05-01T00:00:00Z');
INSERT INTO cases VALUES(7288,1588590634,62,'','',7755,3461,245,'2020-05-02T00:00:00Z');
INSERT INTO cases VALUES(7289,1588590635,62,'','',7781,3587,248,'2020-05-03T00:00:00Z');
INSERT INTO cases VALUES(8950,1588590697,85,'','',1,0,0,'2020-01-27T00:00:00Z');
INSERT INTO cases VALUES(8951,1588590697,85,'','',4,0,0,'2020-01-28T00:00:00Z');
INSERT INTO cases VALUES(8952,1588590697,85,'','',4,0,0,'2020-01-29T00:00:00Z');
INSERT INTO cases VALUES(8953,1588590697,85,'','',4,0,0,'2020-01-30T00:00:00Z');
INSERT INTO cases VALUES(8954,1588590697,85,'','',5,0,0,'2020-01-31T00:00:00Z');
INSERT INTO cases VALUES(8955,1588590697,85,'','',8,0,0,'2020-02-01T00:00:00Z');
INSERT INTO cases VALUES(8956,1588590697,85,'','',10,0,0,'2020-02-02T00:00:00Z');
INSERT INTO cases VALUES(8957,1588590697,85,'','',12,0,0,'2020-02-03T00:00:00Z');
INSERT INTO cases VALUES(8958,1588590697,85,'','',12,0,0,'2020-02-04T00:00:00Z');
INSERT INTO cases VALUES(8959,1588590697,85,'','',12,0,0,'2020-02-05T00:00:00Z');
INSERT INTO cases VALUES(8960,1588590697,85,'','',12,0,0,'2020-02-06T00:00:00Z');
INSERT INTO cases VALUES(8961,1588590697,85,'','',13,0,0,'2020-02-07T00:00:00Z');
INSERT INTO cases VALUES(8962,1588590697,85,'','',13,0,0,'2020-02-08T00:00:00Z');
INSERT INTO cases VALUES(8963,1588590697,85,'','',14,0,0,'2020-02-09T00:00:00Z');
INSERT INTO cases VALUES(8964,1588590697,85,'','',14,0,0,'2020-02-10T00:00:00Z');
INSERT INTO cases VALUES(8965,1588590698,85,'','',16,0,0,'2020-02-11T00:00:00Z');
INSERT INTO cases VALUES(8966,1588590698,85,'','',16,0,0,'2020-02-12T00:00:00Z');
INSERT INTO cases VALUES(8967,1588590698,85,'','',16,1,0,'2020-02-13T00:00:00Z');
INSERT INTO cases VALUES(8968,1588590698,85,'','',16,1,0,'2020-02-14T00:00:00Z');
INSERT INTO cases VALUES(8969,1588590698,85,'','',16,1,0,'2020-02-15T00:00:00Z');
INSERT INTO cases VALUES(8970,1588590698,85,'','',16,1,0,'2020-02-16T00:00:00Z');
INSERT INTO cases VALUES(8971,1588590698,85,'','',16,1,0,'2020-02-17T00:00:00Z');
INSERT INTO cases VALUES(8972,1588590698,85,'','',16,12,0,'2020-02-18T00:00:00Z');
INSERT INTO cases VALUES(8973,1588590698,85,'','',16,12,0,'2020-02-19T00:00:00Z');
INSERT INTO cases VALUES(8974,1588590698,85,'','',16,12,0,'2020-02-20T00:00:00Z');
INSERT INTO cases VALUES(8975,1588590698,85,'','',16,14,0,'2020-02-21T00:00:00Z');
INSERT INTO cases VALUES(8976,1588590698,85,'','',16,14,0,'2020-02-22T00:00:00Z');
INSERT INTO cases VALUES(8977,1588590698,85,'','',16,14,0,'2020-02-23T00:00:00Z');
INSERT INTO cases VALUES(8978,1588590698,85,'','',16,14,0,'2020-02-24T00:00:00Z');
INSERT INTO cases VALUES(8979,1588590698,85,'','',17,14,0,'2020-02-25T00:00:00Z');
INSERT INTO cases VALUES(8980,1588590698,85,'','',27,15,0,'2020-02-26T00:00:00Z');
INSERT INTO cases VALUES(8981,1588590698,85,'','',46,16,0,'2020-02-27T00:00:00Z');
INSERT INTO cases VALUES(8982,1588590698,85,'','',48,16,0,'2020-02-28T00:00:00Z');
INSERT INTO cases VALUES(8983,1588590698,85,'','',79,16,0,'2020-02-29T00:00:00Z');
INSERT INTO cases VALUES(8984,1588590698,85,'','',130,16,0,'2020-03-01T00:00:00Z');
INSERT INTO cases VALUES(8985,1588590698,85,'','',159,16,0,'2020-03-02T00:00:00Z');
INSERT INTO cases VALUES(8986,1588590698,85,'','',196,16,0,'2020-03-03T00:00:00Z');
INSERT INTO cases VALUES(8987,1588590698,85,'','',262,16,0,'2020-03-04T00:00:00Z');
INSERT INTO cases VALUES(8988,1588590698,85,'','',482,16,0,'2020-03-05T00:00:00Z');
INSERT INTO cases VALUES(8989,1588590698,85,'','',670,17,0,'2020-03-06T00:00:00Z');
INSERT INTO cases VALUES(8990,1588590698,85,'','',799,18,0,'2020-03-07T00:00:00Z');
INSERT INTO cases VALUES(8991,1588590699,85,'','',1040,18,0,'2020-03-08T00:00:00Z');
INSERT INTO cases VALUES(8992,1588590699,85,'','',1176,18,2,'2020-03-09T00:00:00Z');
INSERT INTO cases VALUES(8993,1588590699,85,'','',1457,18,2,'2020-03-10T00:00:00Z');
INSERT INTO cases VALUES(8994,1588590699,85,'','',1908,25,3,'2020-03-11T00:00:00Z');
INSERT INTO cases VALUES(8995,1588590699,85,'','',2078,25,3,'2020-03-12T00:00:00Z');
INSERT INTO cases VALUES(8996,1588590699,85,'','',3675,46,7,'2020-03-13T00:00:00Z');
INSERT INTO cases VALUES(8997,1588590699,85,'','',4585,46,9,'2020-03-14T00:00:00Z');
INSERT INTO cases VALUES(8998,1588590699,85,'','',5795,46,11,'2020-03-15T00:00:00Z');
INSERT INTO cases VALUES(8999,1588590699,85,'','',7272,67,17,'2020-03-16T00:00:00Z');
INSERT INTO cases VALUES(9000,1588590699,85,'','',9257,67,24,'2020-03-17T00:00:00Z');
INSERT INTO cases VALUES(9001,1588590699,85,'','',12327,105,28,'2020-03-18T00:00:00Z');
INSERT INTO cases VALUES(9002,1588590699,85,'','',15320,113,44,'2020-03-19T00:00:00Z');
INSERT INTO cases VALUES(9003,1588590699,85,'','',19848,180,67,'2020-03-20T00:00:00Z');
INSERT INTO cases VALUES(9004,1588590699,85,'','',22213,233,84,'2020-03-21T00:00:00Z');
INSERT INTO cases VALUES(9005,1588590699,85,'','',24873,266,94,'2020-03-22T00:00:00Z');
INSERT INTO cases VALUES(9006,1588590699,85,'','',29056,266,123,'2020-03-23T00:00:00Z');
INSERT INTO cases VALUES(9007,1588590699,85,'','',32986,3243,157,'2020-03-24T00:00:00Z');
INSERT INTO cases VALUES(9008,1588590699,85,'','',37323,3547,206,'2020-03-25T00:00:00Z');
INSERT INTO cases VALUES(9009,1588590699,85,'','',43938,5673,267,'2020-03-26T00:00:00Z');
INSERT INTO cases VALUES(9010,1588590699,85,'','',50871,6658,342,'2020-03-27T00:00:00Z');
INSERT INTO cases VALUES(9011,1588590699,85,'','',57695,8481,433,'2020-03-28T00:00:00Z');
INSERT INTO cases VALUES(9012,1588590699,85,'','',62095,9211,533,'2020-03-29T00:00:00Z');
INSERT INTO cases VALUES(9013,1588590699,85,'','',66885,13500,645,'2020-03-30T00:00:00Z');
INSERT INTO cases VALUES(9014,1588590699,85,'','',71808,16100,775,'2020-03-31T00:00:00Z');
INSERT INTO cases VALUES(9015,1588590699,85,'','',77872,18700,920,'2020-04-01T00:00:00Z');
INSERT INTO cases VALUES(9016,1588590700,85,'','',84794,22440,1107,'2020-04-02T00:00:00Z');
INSERT INTO cases VALUES(9017,1588590700,85,'','',91159,24575,1275,'2020-04-03T00:00:00Z');
INSERT INTO cases VALUES(9018,1588590700,85,'','',96092,26400,1444,'2020-04-04T00:00:00Z');
INSERT INTO cases VALUES(9019,1588590700,85,'','',100123,28700,1584,'2020-04-05T00:00:00Z');
INSERT INTO cases VALUES(9020,1588590700,85,'','',103374,28700,1810,'2020-04-06T00:00:00Z');
INSERT INTO cases VALUES(9021,1588590700,85,'','',107663,36081,2016,'2020-04-07T00:00:00Z');
INSERT INTO cases VALUES(9022,1588590700,85,'','',113296,46300,2349,'2020-04-08T00:00:00Z');
INSERT INTO cases VALUES(9023,1588590700,85,'','',118181,52407,2607,'2020-04-09T00:00:00Z');
INSERT INTO cases VALUES(9024,1588590700,85,'','',122171,53913,2767,'2020-04-10T00:00:00Z');
INSERT INTO cases VALUES(9025,1588590700,85,'','',124908,57400,2736,'2020-04-11T00:00:00Z');
INSERT INTO cases VALUES(9026,1588590700,85,'','',127854,60300,3022,'2020-04-12T00:00:00Z');
INSERT INTO cases VALUES(9027,1588590700,85,'','',130072,64300,3194,'2020-04-13T00:00:00Z');
INSERT INTO cases VALUES(9028,1588590700,85,'','',131359,68200,3294,'2020-04-14T00:00:00Z');
INSERT INTO cases VALUES(9029,1588590700,85,'','',134753,72600,3804,'2020-04-15T00:00:00Z');
INSERT INTO cases VALUES(9030,1588590700,85,'','',137698,77000,4052,'2020-04-16T00:00:00Z');
INSERT INTO cases VALUES(9031,1588590700,85,'','',141397,83114,4352,'2020-04-17T00:00:00Z');
INSERT INTO cases VALUES(9032,1588590700,85,'','',143342,85400,4459,'2020-04-18T00:00:00Z');
INSERT INTO cases VALUES(9033,1588590700,85,'','',145184,88000,4586,'2020-04-19T00:00:00Z');
INSERT INTO cases VALUES(9034,1588590700,85,'','',147065,91500,4862,'2020-04-20T00:00:00Z');
INSERT INTO cases VALUES(9035,1588590700,85,'','',148291,95200,5033,'2020-04-21T00:00:00Z');
INSERT INTO cases VALUES(9036,1588590700,85,'','',150648,99400,5279,'2020-04-22T00:00:00Z');
INSERT INTO cases VALUES(9037,1588590700,85,'','',153129,103300,5575,'2020-04-23T00:00:00Z');
INSERT INTO cases VALUES(9038,1588590700,85,'','',154999,109800,5760,'2020-04-24T00:00:00Z');
INSERT INTO cases VALUES(9039,1588590700,85,'','',156513,109800,5877,'2020-04-25T00:00:00Z');
INSERT INTO cases VALUES(9040,1588590700,85,'','',157770,112000,5976,'2020-04-26T00:00:00Z');
INSERT INTO cases VALUES(9041,1588590700,85,'','',158758,114500,6126,'2020-04-27T00:00:00Z');
INSERT INTO cases VALUES(9042,1588590700,85,'','',159912,117400,6314,'2020-04-28T00:00:00Z');
INSERT INTO cases VALUES(9043,1588590700,85,'','',161539,120400,6467,'2020-04-29T00:00:00Z');
INSERT INTO cases VALUES(9044,1588590701,85,'','',163009,123500,6623,'2020-04-30T00:00:00Z');
INSERT INTO cases VALUES(9045,1588590701,85,'','',164077,126900,6736,'2020-05-01T00:00:00Z');
INSERT INTO cases VALUES(9046,1588590701,85,'','',164967,129000,6812,'2020-05-02T00:00:00Z');
INSERT INTO cases VALUES(9047,1588590701,85,'','',165664,130600,6866,'2020-05-03T00:00:00Z');
INSERT INTO cases VALUES(11097,1588590789,130,'','',1,0,0,'2020-02-28T00:00:00Z');
INSERT INTO cases VALUES(11098,1588590789,130,'','',1,0,0,'2020-02-29T00:00:00Z');
INSERT INTO cases VALUES(11099,1588590789,130,'','',1,0,0,'2020-03-01T00:00:00Z');
INSERT INTO cases VALUES(11100,1588590789,130,'','',1,0,0,'2020-03-02T00:00:00Z');
INSERT INTO cases VALUES(11101,1588590789,130,'','',1,0,0,'2020-03-03T00:00:00Z');
INSERT INTO cases VALUES(11102,1588590789,130,'','',1,0,0,'2020-03-04T00:00:00Z');
INSERT INTO cases VALUES(11103,1588590789,130,'','',1,0,0,'2020-03-05T00:00:00Z');
INSERT INTO cases VALUES(11104,1588590789,130,'','',1,0,0,'2020-03-06T00:00:00Z');
INSERT INTO cases VALUES(11105,1588590790,130,'','',1,0,0,'2020-03-07T00:00:00Z');
INSERT INTO cases VALUES(11106,1588590790,130,'','',1,0,0,'2020-03-08T00:00:00Z');
INSERT INTO cases VALUES(11107,1588590790,130,'','',1,0,0,'2020-03-09T00:00:00Z');
INSERT INTO cases VALUES(11108,1588590790,130,'','',1,0,0,'2020-03-10T00:00:00Z');
INSERT INTO cases VALUES(11109,1588590790,130,'','',3,0,0,'2020-03-11T00:00:00Z');
INSERT INTO cases VALUES(11110,1588590790,130,'','',3,0,0,'2020-03-12T00:00:00Z');
INSERT INTO cases VALUES(11111,1588590790,130,'','',6,0,0,'2020-03-13T00:00:00Z');
INSERT INTO cases VALUES(11112,1588590790,130,'','',8,0,0,'2020-03-14T00:00:00Z');
INSERT INTO cases VALUES(11113,1588590790,130,'','',12,1,0,'2020-03-15T00:00:00Z');
INSERT INTO cases VALUES(11114,1588590790,130,'','',17,1,0,'2020-03-16T00:00:00Z');
INSERT INTO cases VALUES(11115,1588590790,130,'','',25,1,0,'2020-03-17T00:00:00Z');
INSERT INTO cases VALUES(11116,1588590790,130,'','',27,1,0,'2020-03-18T00:00:00Z');
INSERT INTO cases VALUES(11117,1588590790,130,'','',36,1,0,'2020-03-19T00:00:00Z');
INSERT INTO cases VALUES(11118,1588590790,130,'','',49,1,0,'2020-03-20T00:00:00Z');
INSERT INTO cases VALUES(11119,1588590791,130,'','',83,1,1,'2020-03-21T00:00:00Z');
INSERT INTO cases VALUES(11120,1588590791,130,'','',143,1,1,'2020-03-22T00:00:00Z');
INSERT INTO cases VALUES(11121,1588590791,130,'','',179,1,1,'2020-03-23T00:00:00Z');
INSERT INTO cases VALUES(11122,1588590791,130,'','',209,1,2,'2020-03-24T00:00:00Z');
INSERT INTO cases VALUES(11123,1588590791,130,'','',274,1,4,'2020-03-25T00:00:00Z');
INSERT INTO cases VALUES(11124,1588590791,130,'','',299,1,4,'2020-03-26T00:00:00Z');
INSERT INTO cases VALUES(11125,1588590791,130,'','',358,1,5,'2020-03-27T00:00:00Z');
INSERT INTO cases VALUES(11126,1588590791,130,'','',394,1,7,'2020-03-28T00:00:00Z');
INSERT INTO cases VALUES(11127,1588590791,130,'','',460,1,7,'2020-03-29T00:00:00Z');
INSERT INTO cases VALUES(11128,1588590791,130,'','',491,7,7,'2020-03-30T00:00:00Z');
INSERT INTO cases VALUES(11129,1588590791,130,'','',537,7,8,'2020-03-31T00:00:00Z');
INSERT INTO cases VALUES(11130,1588590791,130,'','',581,7,8,'2020-04-01T00:00:00Z');
INSERT INTO cases VALUES(11131,1588590791,130,'','',649,7,9,'2020-04-02T00:00:00Z');
INSERT INTO cases VALUES(11132,1588590791,130,'','',696,7,9,'2020-04-03T00:00:00Z');
INSERT INTO cases VALUES(11133,1588590792,130,'','',771,7,11,'2020-04-04T00:00:00Z');
INSERT INTO cases VALUES(11134,1588590792,130,'','',811,7,13,'2020-04-05T00:00:00Z');
INSERT INTO cases VALUES(11135,1588590792,130,'','',843,8,15,'2020-04-06T00:00:00Z');
INSERT INTO cases VALUES(11136,1588590792,130,'','',880,8,15,'2020-04-07T00:00:00Z');
INSERT INTO cases VALUES(11137,1588590792,130,'','',912,8,15,'2020-04-08T00:00:00Z');
INSERT INTO cases VALUES(11138,1588590792,130,'','',955,8,16,'2020-04-09T00:00:00Z');
INSERT INTO cases VALUES(11139,1588590792,130,'','',999,54,22,'2020-04-10T00:00:00Z');
INSERT INTO cases VALUES(11140,1588590792,130,'','',1026,54,23,'2020-04-11T00:00:00Z');
INSERT INTO cases VALUES(11141,1588590792,130,'','',1053,97,23,'2020-04-12T00:00:00Z');
INSERT INTO cases VALUES(11142,1588590792,130,'','',1062,101,24,'2020-04-13T00:00:00Z');
INSERT INTO cases VALUES(11143,1588590792,130,'','',1070,101,29,'2020-04-14T00:00:00Z');
INSERT INTO cases VALUES(11144,1588590792,130,'','',1091,138,30,'2020-04-15T00:00:00Z');
INSERT INTO cases VALUES(11145,1588590792,130,'','',1128,178,32,'2020-04-16T00:00:00Z');
INSERT INTO cases VALUES(11146,1588590792,130,'','',1149,210,33,'2020-04-17T00:00:00Z');
INSERT INTO cases VALUES(11147,1588590792,130,'','',1239,228,33,'2020-04-18T00:00:00Z');
INSERT INTO cases VALUES(11148,1588590792,130,'','',1298,242,35,'2020-04-19T00:00:00Z');
INSERT INTO cases VALUES(11149,1588590792,130,'','',1326,242,37,'2020-04-20T00:00:00Z');
INSERT INTO cases VALUES(11150,1588590792,130,'','',1350,298,38,'2020-04-21T00:00:00Z');
INSERT INTO cases VALUES(11151,1588590792,130,'','',1370,357,38,'2020-04-22T00:00:00Z');
INSERT INTO cases VALUES(11152,1588590792,130,'','',1398,399,40,'2020-04-23T00:00:00Z');
INSERT INTO cases VALUES(11153,1588590792,130,'','',1410,430,40,'2020-04-24T00:00:00Z');
INSERT INTO cases VALUES(11154,1588590792,130,'','',1426,460,41,'2020-04-25T00:00:00Z');
INSERT INTO cases VALUES(11155,1588590792,130,'','',1438,467,41,'2020-04-26T00:00:00Z');
INSERT INTO cases VALUES(11156,1588590792,130,'','',1449,474,41,'2020-04-27T00:00:00Z');
INSERT INTO cases VALUES(11157,1588590792,130,'','',1344,536,44,'2020-04-28T00:00:00Z');
INSERT INTO cases VALUES(11158,1588590793,130,'','',1375,563,45,'2020-04-29T00:00:00Z');
INSERT INTO cases VALUES(11159,1588590793,130,'','',1385,589,45,'2020-04-30T00:00:00Z');
INSERT INTO cases VALUES(11160,1588590793,130,'','',1399,594,45,'2020-05-01T00:00:00Z');
INSERT INTO cases VALUES(11161,1588590793,130,'','',1406,632,46,'2020-05-02T00:00:00Z');
INSERT INTO cases VALUES(11162,1588590793,130,'','',1410,635,46,'2020-05-03T00:00:00Z');
INSERT INTO cases VALUES(13359,1588590893,179,'','',1,0,0,'2020-03-04T00:00:00Z');
INSERT INTO cases VALUES(13360,1588590893,179,'','',1,0,0,'2020-03-05T00:00:00Z');
INSERT INTO cases VALUES(13361,1588590893,179,'','',5,0,0,'2020-03-06T00:00:00Z');
INSERT INTO cases VALUES(13362,1588590893,179,'','',5,0,0,'2020-03-07T00:00:00Z');
INSERT INTO cases VALUES(13363,1588590893,179,'','',11,0,0,'2020-03-08T00:00:00Z');
INSERT INTO cases VALUES(13364,1588590893,179,'','',16,0,0,'2020-03-09T00:00:00Z');
INSERT INTO cases VALUES(13365,1588590893,179,'','',22,0,0,'2020-03-10T00:00:00Z');
INSERT INTO cases VALUES(13366,1588590893,179,'','',31,0,0,'2020-03-11T00:00:00Z');
INSERT INTO cases VALUES(13367,1588590893,179,'','',49,0,1,'2020-03-12T00:00:00Z');
INSERT INTO cases VALUES(13368,1588590893,179,'','',68,0,2,'2020-03-13T00:00:00Z');
INSERT INTO cases VALUES(13369,1588590893,179,'','',103,0,3,'2020-03-14T00:00:00Z');
INSERT INTO cases VALUES(13370,1588590893,179,'','',119,0,3,'2020-03-15T00:00:00Z');
INSERT INTO cases VALUES(13371,1588590893,179,'','',177,13,4,'2020-03-16T00:00:00Z');
INSERT INTO cases VALUES(13372,1588590893,179,'','',238,13,5,'2020-03-17T00:00:00Z');
INSERT INTO cases VALUES(13373,1588590893,179,'','',251,13,5,'2020-03-18T00:00:00Z');
INSERT INTO cases VALUES(13374,1588590893,179,'','',355,1,5,'2020-03-19T00:00:00Z');
INSERT INTO cases VALUES(13375,1588590893,179,'','',425,1,5,'2020-03-20T00:00:00Z');
INSERT INTO cases VALUES(13376,1588590894,179,'','',536,1,5,'2020-03-21T00:00:00Z');
INSERT INTO cases VALUES(13377,1588590894,179,'','',634,1,7,'2020-03-22T00:00:00Z');
INSERT INTO cases VALUES(13378,1588590894,179,'','',749,1,8,'2020-03-23T00:00:00Z');
INSERT INTO cases VALUES(13379,1588590894,179,'','',901,1,10,'2020-03-24T00:00:00Z');
INSERT INTO cases VALUES(13380,1588590894,179,'','',1051,7,14,'2020-03-25T00:00:00Z');
INSERT INTO cases VALUES(13381,1588590894,179,'','',1221,7,16,'2020-03-26T00:00:00Z');
INSERT INTO cases VALUES(13382,1588590894,179,'','',1389,7,16,'2020-03-27T00:00:00Z');
INSERT INTO cases VALUES(13383,1588590894,179,'','',1638,7,18,'2020-03-28T00:00:00Z');
INSERT INTO cases VALUES(13384,1588590894,179,'','',1862,7,22,'2020-03-29T00:00:00Z');
INSERT INTO cases VALUES(13385,1588590894,179,'','',2055,7,31,'2020-03-30T00:00:00Z');
INSERT INTO cases VALUES(13386,1588590894,179,'','',2311,7,33,'2020-03-31T00:00:00Z');
INSERT INTO cases VALUES(13387,1588590894,179,'','',2554,47,43,'2020-04-01T00:00:00Z');
INSERT INTO cases VALUES(13388,1588590894,179,'','',2946,56,57,'2020-04-02T00:00:00Z');
INSERT INTO cases VALUES(13389,1588590894,179,'','',3383,56,71,'2020-04-03T00:00:00Z');
INSERT INTO cases VALUES(13390,1588590894,179,'','',3627,116,79,'2020-04-04T00:00:00Z');
INSERT INTO cases VALUES(13391,1588590894,179,'','',4102,134,94,'2020-04-05T00:00:00Z');
INSERT INTO cases VALUES(13392,1588590894,179,'','',4413,162,107,'2020-04-06T00:00:00Z');
INSERT INTO cases VALUES(13393,1588590894,179,'','',4848,191,129,'2020-04-07T00:00:00Z');
INSERT INTO cases VALUES(13394,1588590894,179,'','',5205,222,159,'2020-04-08T00:00:00Z');
INSERT INTO cases VALUES(13395,1588590894,179,'','',5575,284,174,'2020-04-09T00:00:00Z');
INSERT INTO cases VALUES(13396,1588590894,179,'','',5955,318,181,'2020-04-10T00:00:00Z');
INSERT INTO cases VALUES(13397,1588590895,179,'','',6356,375,208,'2020-04-11T00:00:00Z');
INSERT INTO cases VALUES(13398,1588590895,179,'','',6674,439,232,'2020-04-12T00:00:00Z');
INSERT INTO cases VALUES(13399,1588590895,179,'','',6934,487,245,'2020-04-13T00:00:00Z');
INSERT INTO cases VALUES(13400,1588590895,179,'','',7202,618,263,'2020-04-14T00:00:00Z');
INSERT INTO cases VALUES(13401,1588590895,179,'','',7582,668,286,'2020-04-15T00:00:00Z');
INSERT INTO cases VALUES(13402,1588590895,179,'','',7918,774,314,'2020-04-16T00:00:00Z');
INSERT INTO cases VALUES(13403,1588590895,179,'','',8379,866,332,'2020-04-17T00:00:00Z');
INSERT INTO cases VALUES(13404,1588590895,179,'','',8742,981,347,'2020-04-18T00:00:00Z');
INSERT INTO cases VALUES(13405,1588590895,179,'','',9287,1040,360,'2020-04-19T00:00:00Z');
INSERT INTO cases VALUES(13406,1588590895,179,'','',9593,1133,380,'2020-04-20T00:00:00Z');
INSERT INTO cases VALUES(13407,1588590895,179,'','',9856,1297,401,'2020-04-21T00:00:00Z');
INSERT INTO cases VALUES(13408,1588590895,179,'','',10169,1513,426,'2020-04-22T00:00:00Z');
INSERT INTO cases VALUES(13409,1588590895,179,'','',10511,1740,454,'2020-04-23T00:00:00Z');
INSERT INTO cases VALUES(13410,1588590895,179,'','',10892,1944,494,'2020-04-24T00:00:00Z');
INSERT INTO cases VALUES(13411,1588590895,179,'','',11273,2126,524,'2020-04-25T00:00:00Z');
INSERT INTO cases VALUES(13412,1588590895,179,'','',11617,2265,535,'2020-04-26T00:00:00Z');
INSERT INTO cases VALUES(13413,1588590895,179,'','',11902,2466,562,'2020-04-27T00:00:00Z');
INSERT INTO cases VALUES(13414,1588590895,179,'','',12218,2655,596,'2020-04-28T00:00:00Z');
INSERT INTO cases VALUES(13415,1588590895,179,'','',12640,3025,624,'2020-04-29T00:00:00Z');
INSERT INTO cases VALUES(13416,1588590895,179,'','',12877,3236,644,'2020-04-30T00:00:00Z');
INSERT INTO cases VALUES(13417,1588590895,179,'','',13105,3491,651,'2020-05-01T00:00:00Z');
INSERT INTO cases VALUES(13418,1588590895,179,'','',13375,3762,664,'2020-05-02T00:00:00Z');
INSERT INTO cases VALUES(13419,1588590895,179,'','',13693,3945,678,'2020-05-03T00:00:00Z');
INSERT INTO cases VALUES(129551,1588614431,62,'','',7781,3587,248,'2020-05-04T17:46:24Z');
INSERT INTO cases VALUES(129570,1588614433,85,'','',165664,132700,6866,'2020-05-04T17:46:24Z');
INSERT INTO cases VALUES(129604,1588614438,130,'','',1410,635,46,'2020-05-04T17:46:24Z');
INSERT INTO cases VALUES(129736,1588767029,62,'','',7896,4006,257,'2020-05-06T11:51:18Z');
INSERT INTO cases VALUES(129755,1588767031,85,'','',167007,135100,6993,'2020-05-06T11:51:18Z');
INSERT INTO cases VALUES(129789,1588767034,130,'','',1423,678,46,'2020-05-06T11:51:18Z');
INSERT INTO cases VALUES(129824,1588767037,179,'','',14431,4280,716,'2020-05-06T11:51:18Z');
