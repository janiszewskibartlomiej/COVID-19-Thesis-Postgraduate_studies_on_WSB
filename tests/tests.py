import time
import unittest
import os
import pandas
import plotly
import plotly.graph_objects as go
from test_methods import TestMethods
from connect_to_db import ConnectToDb
from data_processing import DataProcessing
from graphs import Graphs

path_root = os.path.abspath("..")
# x = x.replace('\\', '/')
print(path_root)
os.chdir(path_root)


class DataProcessingTestCase(unittest.TestCase):
    def setUp(self):
        self.conn = ConnectToDb()
        self.data_processing = DataProcessing()
        self.test_methods = TestMethods()

    def test_get_icon_color(self):
        self.assertEqual(self.data_processing.get_icon_color(1), "#29a329")
        self.assertEqual(self.data_processing.get_icon_color(999), "#29a329")
        self.assertEqual(self.data_processing.get_icon_color(1000), "#196619")
        self.assertEqual(self.data_processing.get_icon_color(4999), "#196619")
        self.assertEqual(self.data_processing.get_icon_color(5000), "#f2c718")
        self.assertEqual(self.data_processing.get_icon_color(9999), "#f2c718")
        self.assertEqual(self.data_processing.get_icon_color(10000), "#ffcc00")
        self.assertEqual(self.data_processing.get_icon_color(24999), "#ffcc00")
        self.assertEqual(self.data_processing.get_icon_color(25000), "#ff9900")
        self.assertEqual(self.data_processing.get_icon_color(49999), "#ff9900")
        self.assertEqual(self.data_processing.get_icon_color(50000), "#ff5c33")
        self.assertEqual(self.data_processing.get_icon_color(99999), "#ff5c33")
        self.assertEqual(self.data_processing.get_icon_color(100000), "#ff3300")
        self.assertEqual(self.data_processing.get_icon_color(149999), "#ff3300")
        self.assertEqual(self.data_processing.get_icon_color(150000), "#ff3333")
        self.assertEqual(self.data_processing.get_icon_color(249999), "#ff3333")
        self.assertEqual(self.data_processing.get_icon_color(250000), "#ff0000")
        self.assertEqual(self.data_processing.get_icon_color(100 ** 4), "#ff0000")

    def test_select_all_records_where_declare_id(self):
        country_id = self.test_methods.get_country_id()
        query = self.conn.select_all_records(
            query="SELECT *, max(last_update) FROM cases WHERE country_id = ?",
            parameter=(country_id,),
        )
        self.assertIsNotNone(query)
        self.assertEqual(query[0][2], country_id)
        self.assertTrue(query, list)

    def test_dataframe_diff(self):
        country_id = self.test_methods.get_country_id()
        data = self.data_processing.all_cases_per_day_where_country_id_equal(
            country_id=country_id
        )
        self.assertIsNotNone(data)
        self.assertNotEqual(data, [])
        df = self.data_processing.get_dateframe(data=data)
        verify_df = str(type(df)).replace(">", "").replace("'", "").split(".")
        self.assertIn("DataFrame", verify_df)
        self.assertIsNotNone(df)
        self.assertListEqual(
            ["Confirmed", "Deaths", "Recovered", "Date"], [x for x in df.columns]
        )
        df_diff = self.data_processing.get_dateframe_diff(data=data)
        self.assertIsNotNone(df_diff)
        self.assertEqual(df_diff.columns[-1], "Date")
        df.to_csv(path_or_buf="tests/poland_df.csv", encoding="utf-8")
        search = os.path.abspath("tests/poland_df.csv")
        self.assertTrue(os.path.exists(search))
        assert "poland_df.csv" in search
        df_diff.to_csv(path_or_buf="tests/poland_diff.csv", encoding="utf-8")
        search2 = os.path.abspath("tests/poland_diff.csv")
        self.assertIn("poland_diff.csv", search2)
        self.assertTrue(os.path.exists(search2))

    def test_dataframe(self):
        country_id = self.test_methods.get_country_id()
        data = self.data_processing.all_cases_per_day_where_country_id_equal(
            country_id=country_id
        )
        df = self.data_processing.get_dateframe(data=data)
        self.assertIsNotNone(df)
        self.assertTrue(isinstance(df, pandas.DataFrame))

    def test_coordinates(self):
        location = self.test_methods.get_location()
        test_location = self.data_processing.slice_location(location)
        self.assertTrue(isinstance(test_location[0], float))
        self.assertTrue(isinstance(test_location[1], float))
        test_location_str = str(test_location)
        self.assertEqual(test_location_str, location)
        test_location2 = self.data_processing.slice_location("[54.0, -2.0]")
        self.assertEqual(test_location2, [54.0, -2.0])

    def test_total_current_cases(self):
        data = self.data_processing.total_current_cases()
        self.assertIsNotNone(data)
        self.assertTrue(isinstance(data, list))
        assert data.__len__() > 0
        verify_data = data[0]
        self.assertTrue(isinstance(verify_data[0], int))
        self.assertTrue(isinstance(verify_data[1], str))
        self.assertTrue(isinstance(verify_data[2], str))
        self.assertTrue(isinstance(verify_data[3], int))
        self.assertTrue(isinstance(verify_data[4], int))
        self.assertTrue(isinstance(verify_data[5], int))
        self.assertTrue(isinstance(verify_data[6], str))
        self.assertTrue(isinstance(verify_data[7], str))
        self.assertTrue(isinstance(verify_data[8], str))
        self.assertIn("https", verify_data[8])

    def test_total_per_day(self):
        data = self.data_processing.total_cases_per_day()
        self.assertIsNotNone(data)
        self.assertTrue(isinstance(data, list))
        self.assertTrue(isinstance(data[0][0], int))
        self.assertTrue(isinstance(data[0][1], int))
        self.assertTrue(isinstance(data[0][2], int))
        self.assertTrue(isinstance(data[0][3], str))
        self.assertTrue(isinstance(data[0], tuple))
        assert data.__len__() > 0
        self.assertTrue(time.strftime(data[0][3]))

    def test_name_3code_country(self):
        country_id = self.test_methods.get_country_id()
        print(country_id)
        data = self.data_processing.get_name_and_3code_country(country_id=country_id)
        self.assertTrue(isinstance(data[0], str))
        self.assertTrue(isinstance(data[1], str))
        self.assertTrue(isinstance(data, tuple))
        self.assertIsNotNone(data)

    def test_id_name_countries(self):
        data = self.data_processing.get_id_and_name_of_countries()
        self.assertIsNotNone(data)
        self.assertTrue(isinstance(data, list))
        self.assertTrue(isinstance(data[0], tuple))
        self.assertTrue(data[0][0], int)
        self.assertTrue(data[0][1], str)
        assert data.__len__() > 0


class GraphsTestCase(unittest.TestCase):
    def setUp(self):
        self.graphs = Graphs()
        self.test_methods = TestMethods()
        self.data_processing = DataProcessing()

    def test_write_grap(self):
        title = "write_test"
        file = "templates/graphs/write_test.html"
        self.graphs.write_graph_to_html(figure=go.Figure(), title=title)
        search = os.path.abspath(file)
        self.assertIn(title, search)
        self.assertTrue(os.path.exists(search))
        os.remove(file)
        self.assertFalse(os.path.isfile(file))

    def test_figure(self):
        country_id = self.test_methods.get_country_id()
        self.assertTrue(isinstance(country_id, int))
        data = self.data_processing.all_cases_per_day_where_country_id_equal(
            country_id=country_id
        )
        self.assertTrue(isinstance(data, list))
        self.assertTrue(isinstance(data[0], tuple))
        assert len(data) > 0
        dataframe = self.data_processing.get_dateframe(data=data)
        self.assertTrue(isinstance(dataframe, pandas.DataFrame))
        alpha_3_code = ConnectToDb().select_one_record(
            query=r"SELECT co.alpha_3_code from countries as co join cases as ca on co.country_id = ca.country_id group by co.country_id having co.country_id = ?",
            parameter=(country_id,),
        )
        self.assertTrue(isinstance(alpha_3_code[0], str))
        figure = self.graphs.creating_figure_with_data(
            figure=go.Figure(), dataframe=dataframe, alpha_3_code=alpha_3_code[0]
        )
        self.assertTrue(isinstance(figure, plotly.graph_objects.Figure))

    def test_graph(self):
        country_id = self.test_methods.get_country_id()
        data = self.data_processing.all_cases_per_day_where_country_id_equal(
            country_id=country_id
        )
        dataframe = self.data_processing.get_dateframe(data=data)
        graph = self.graphs.get_graph(
            country_id=country_id, dataframe=dataframe, diff=False, write=False
        )
        self.assertTrue(isinstance(graph, tuple))
        self.assertTrue(isinstance(graph[1], str))
        self.assertTrue(isinstance(graph[0], plotly.graph_objects.Figure))

    def test_diff_graph(self):
        country_id = self.test_methods.get_country_id()
        data = self.data_processing.all_cases_per_day_where_country_id_equal(
            country_id=country_id
        )
        dataframe = self.data_processing.get_dateframe_diff(data=data)
        path = "tests/test-diff.csv"
        dataframe.to_csv(path_or_buf=path, encoding="utf-8")
        search = os.path.abspath(path)
        self.assertTrue(os.path.exists(search))
        os.remove(search)
        graph = self.graphs.get_graph(
            country_id=country_id, dataframe=dataframe, diff=True, write=False
        )
        self.assertTrue(isinstance(graph, tuple))
        self.assertTrue(isinstance(graph[1], str))
        self.assertTrue(isinstance(graph[0], plotly.graph_objects.Figure))

    def test_join_graphs(self):
        country_id1 = self.test_methods.get_country_id()
        country_id2 = self.test_methods.get_country_id()
        graph = self.graphs.join_two_graphs(
            first_country_id=country_id1, second_country_id=country_id2
        )
        self.assertTrue(isinstance(graph, tuple))
        self.assertTrue(isinstance(graph[1], str))
        self.assertTrue(isinstance(graph[0], plotly.graph_objects.Figure))
        os.remove("templates/graphs/" + graph[1] + ".html")

    def test_cases_world(self):
        world = self.graphs.cases_of_the_world(write=False)
        self.assertTrue(world)
        self.assertTrue(isinstance(world, tuple))
        self.assertTrue(isinstance(world[0], plotly.graph_objects.Figure))


if __name__ == "__main__":
    unittest.main()
