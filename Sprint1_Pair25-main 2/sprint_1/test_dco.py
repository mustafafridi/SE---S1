import unittest
from unittest.mock import patch
from dbc import Dbc
from dco import Dco

class TestDco(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_url = "https://ows.rasdaman.org"
        cls.dbc = Dbc(cls.server_url)
        cls.dco = Dco(cls.dbc)

    @patch("dbc.Dbc.execute_query_csv")
    def test_getMainAvgTempColor(self, mock_execute_query_csv):
        self.dco.getMainAvgTempColor(53.08, 8.80)
        mock_execute_query_csv.assert_called_once()

    @patch("dbc.Dbc.execute_query_print")
    def test_getMinTempColor(self, mock_execute_query_print):
        self.dco.getMinTempColor(53.08, 8.80)
        mock_execute_query_print.assert_called_once()

    @patch("dbc.Dbc.execute_query_print")
    def test_getMaxTempColor(self, mock_execute_query_print):
        self.dco.getMaxTempColor(53.08, 8.80)
        mock_execute_query_print.assert_called_once()

    @patch("dbc.Dbc.execute_query_print")
    def test_getAverageAvgTempColor(self, mock_execute_query_print):
        self.dco.getAverageAvgTempColor(53.08, 8.80)
        mock_execute_query_print.assert_called_once()

if __name__ == "__main__":
    unittest.main()