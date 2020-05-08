import unittest
import random
from connect_to_db import ConnectToDb
from data_processing import DataProcessing


class DataProcesingTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.dp = DataProcessing()
        self.conn = ConnectToDb()
        self.data_processing = DataProcessing()

    def test_get_icon_color(self):
        self.assertEqual(self.dp.get_icon_color(1), '#29a329')
        self.assertEqual(self.dp.get_icon_color(999), '#29a329')
        self.assertEqual(self.dp.get_icon_color(1000), '#196619')
        self.assertEqual(self.dp.get_icon_color(4999), '#196619')
        self.assertEqual(self.dp.get_icon_color(5000), '#f2c718')
        self.assertEqual(self.dp.get_icon_color(9999), '#f2c718')
        self.assertEqual(self.dp.get_icon_color(10000), '#ffcc00')
        self.assertEqual(self.dp.get_icon_color(24999), '#ffcc00')
        self.assertEqual(self.dp.get_icon_color(25000), '#ff9900')
        self.assertEqual(self.dp.get_icon_color(49999), '#ff9900')
        self.assertEqual(self.dp.get_icon_color(50000), '#ff5c33')
        self.assertEqual(self.dp.get_icon_color(99999), '#ff5c33')
        self.assertEqual(self.dp.get_icon_color(100000), '#ff3300')
        self.assertEqual(self.dp.get_icon_color(149999), '#ff3300')
        self.assertEqual(self.dp.get_icon_color(150000), '#ff3333')
        self.assertEqual(self.dp.get_icon_color(249999), '#ff3333')
        self.assertEqual(self.dp.get_icon_color(250000), '#ff0000')
        self.assertEqual(self.dp.get_icon_color(100 ** 4), '#ff0000')

    def test_connection_db(self):
        country_id = random.randint(1, 250)
        print(country_id)
        query = self.conn.select_all_records(query='SELECT *, max(last_update) FROM cases WHERE country_id = ?',
                                             parameter=(country_id,))
        self.assertIsNotNone(query)
        self.assertEqual(query[2], country_id)

    def test_dataframe(self):
        data = self.data_processing.all_cases_per_day_where_country_id_equal(country_id=179)
        df = self.data_processing.get_dateframe(data=data)
        print(df)

        df_diff = self.data_processing.get_dateframe_diff(data=data)
        print(df_diff)

        df.to_csv(path_or_buf='tests/poland_df.csv', encoding='utf-8')
        df_diff.to_csv(path_or_buf='tests/poland_diff.csv', encoding='utf-8')

        if __name__ == '__main__':
            unittest.main()
