## lista klas i metod:


### Klasa ConnectToDb:
	* __init__                << inicjalizacja zadeklarowanych zmiennych 
	* close_connect           << zamknięcie połączenia z bazą danych
	* commit                  << zapis rekordu w bazie danych
	* delete_record           << kasowanie rekordu w bazie danych
	* execute_script          << wykonanie zapytanie do bazy na podstawie query SQL
	* insert_record           << wysłanie rekordu do bazy danych wraz z zapisem
	* row_factory             << ustawienie SQLite na fukcję pobierania obiektu [nazwy kolumn + rekordy]
	* run_sql_script          << uruchomienie skryptu SQL 
	* select_all_records      << pobieranie wielu rekordów z bazy
	* select_one_record       << pobranie tylko jednego rekordu


### Klasa ImporterOfCountries:
	* load_countries_from_api   << załadowanie danych z API kraje i stworzenie listy własnych słowników z kluczami, które będą wykorzystane wprowadzenie danych.
	* insert_countries_to_db    << wysłanie rekordów i ich zapisa w bazie danych 


### Klasa ImporterAllCases:
	* __init__                                    << inicjalizacja zadeklarowanych i dziedziczonych zmiennych 
	* create_dict_of_countries_name_and_id
	* creating_row_to_insert_db
	* load_all_data_from_json_and_insert_to_db
	* load_data_and_write_json
	* load_name_and_id_of_countries
	* read_json_api
	* read_json_file


### Klasa ImporterCurrentCases:
	* __init__                                      << inicjalizacja zadeklarowanych i dziedziczonych zmiennych
	* load_current_data_from_json_and_insert_to_db


### Klasa DataProcessing:
	* __init__                                      << inicjalizacja zadeklarowanych i dziedziczonych zmiennych
	* all_cases_per_day_where_country_id_equal
	* get_dateframe
	* get_dateframe_diff
	* get_icon_color
	* get_id_and_name_of_country
	* get_name_and_3code_country
	* slice_location
	* total_cases_per_day
	* total_current_cases


### Klasa CreatingMap:
	* __init__              << inicjalizacja zadeklarowanych i dzidziczonych zmiennych
	* map_of_the_world


### Klasa Graphs:
	* __init__                      << inicjalizacja zadeklarowanych i dziedziczonych zmiennych
	* cases_of_the_world
	* creating_figure_with_data
	* get_graph
	* join_two_graphs
	* write_graph_to_html
