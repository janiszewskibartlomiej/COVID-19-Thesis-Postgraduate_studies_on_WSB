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
	* create_dict_of_countries_name_and_id        << stworzenie słownika z kluczem w postaci nazwy i wartoscią z 'id' kraju z bazy
	* creating_row_to_insert_db                   << stworzenie rekordu zgodnego ze strukturą w bazie danych
	* load_all_data_from_json_and_insert_to_db    << załadowanie wszytsich danych z API JSON i zapis rekordów w bazie danych według storzonej struktury, wraz z walidacją i niezapisywaniem rekordów z wartościami zerowymi
	* load_data_and_write_json                    << załadowanie danych z API JSON i zapis do pliku
	* load_alpha2code_and_id_of_countries         << załadowanie listy kodów państw [dwu literowych] i ich 'id'
	* read_json_api                               << odczyt danych z API JSON 
	* read_json_file                              << odczyt danych z pliku JSON 


### Klasa ImporterCurrentCases:
	* __init__                                      << inicjalizacja zadeklarowanych i dziedziczonych zmiennych
	* load_current_data_from_json_and_insert_to_db  << ladowanie danych z API JSON i ich zapis w bazie danych według storzonej struktury, wraz z walidacją rekordów i usuwaniem duplikatów w danym dniu


### Klasa DataProcessing:
	* __init__                                      << inicjalizacja zadeklarowanych i dziedziczonych zmiennych
	* all_cases_per_day_where_country_id_equal      << pobieranie wszytskich przypadków z podziałem na dni dla zadeklarowanego 'id' kraju 
	* get_dateframe                                 << tworzenie ramki danych z podanego źródła
	* get_dateframe_diff                            << tworzenie ramki danych wyliczonymi różnicami pomiędzy wierszami [ilość przypadków w danym dniu] 
	* get_icon_color                                << pobieranie koloru ikony [z własnego słownika] w zależności od ilości zachorowanych 
	* get_id_and_name_of_countries                  << pobieranie listy krajów z ich nazwą  i 'id' 
	* get_name_and_3code_country                    << pobieranie nazwy kraju i kodu trzy literowego po wskazanym 'id' kraju 
	* slice_location                                << tworzenie listy z szerokością i długościa geograficzną na podstawie przekazanego stringa 
	* total_cases_per_day                           << pobieranie wszystkih przypadków z bazy danych i ich grupowanie względem dni
	* total_current_cases                           << pobieranie wszytskich przypadków, które sa w dniu obecnym i pogrupowanie na względem 'id' kraju


### Klasa CreatingMap:
	* __init__              << inicjalizacja zadeklarowanych i dzidziczonych zmiennych
	* map_of_the_world      << tworzenie mapy świata świata wraz z trzema różnymi markerami, nagłówiem, przycisków, zestawieniami dla całego świata oraz danymi dla konkretnego kraju.  


### Klasa Graphs:
	* __init__                      << inicjalizacja zadeklarowanych i dziedziczonych zmiennych
	* cases_of_the_world            << generowanie wykresu dla całego świata
	* creating_figure_with_data     << tworzenie obiektu 'Figure' w bibliotece 'Plotly' wraz z deklaracją wyświetlanych parammetrów wykresu
	* get_graph                     << generowanie wykresu dla danego kraju 
	* join_two_graphs               << generowanie połączonych wykresów na podstawie zadeklarowanych  krajów
	* write_graph_to_html           << zapis wykresu do pliku html
