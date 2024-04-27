#test_dbc.py

import unittest
from unittest.mock import patch
from dbc import Dbc

class TestDbc(unittest.TestCase):
    @patch("requests.post")
    def test_execute_query_csv_success(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.content = b'sample,content'

        dbc = Dbc("http://test-server.com")
        dbc.execute_query_csv("sample query")

        mock_post.assert_called_once_with("http://test-server.com", data={'query': 'sample query'})
        # You might want to add additional assertions here, such as checking if the file was saved successfully.

    @patch("requests.post")
    def test_execute_query_csv_failure(self, mock_post):
        mock_post.return_value.status_code = 500
        mock_post.return_value.text = "Internal Server Error"

        dbc = Dbc("http://test-server.com")
        dbc.execute_query_csv("sample query")

        mock_post.assert_called_once_with("http://test-server.com", data={'query': 'sample query'})
        # You might want to add additional assertions here, such as checking if the error message was printed.

    @patch("requests.post")
    def test_execute_query_print_success(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.content = b'sample,content'

        dbc = Dbc("http://test-server.com")
        dbc.execute_query_print("sample query")

        mock_post.assert_called_once_with("http://test-server.com", data={'query': 'sample query'})
        # You might want to add additional assertions here, such as checking if the content was printed.

    @patch("requests.post")
    def test_execute_query_print_failure(self, mock_post):
        mock_post.return_value.status_code = 500
        mock_post.return_value.text = "Internal Server Error"

        dbc = Dbc("http://test-server.com")
        dbc.execute_query_print("sample query")

        mock_post.assert_called_once_with("http://test-server.com", data={'query': 'sample query'})
        # You might want to add additional assertions here, such as checking if the error message was printed.

if __name__ == "_main_":
    unittest.main()