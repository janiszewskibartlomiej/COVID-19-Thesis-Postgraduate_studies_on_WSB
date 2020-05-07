import unittest
from data_processing import DataProcessing

class DataProcesingTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.dp = DataProcessing()

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


if __name__ == '__main__':
    unittest.main()
