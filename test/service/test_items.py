import unittest
from unittest.mock import MagicMock, patch
import src.service.items as under_test

class ItemsTest(unittest.TestCase):

    @patch("src.service.items.connect_to_db")
    @patch("src.service.items.Reader")
    def test_fetch_all(self, mock_connect_to_db, mock_reader_class):
        mock_conn = MagicMock()
        mock_connect_to_db.return_value = mock_conn

        mock_reader = MagicMock()
        mock_reader.read.return_value = "mocked data"
        mock_reader_class.return_value = mock_reader

        result = under_test.run()
        self.assertEqual("", result)

    def test_sample(self):
        result = under_test.dummy_method_test()
        self.assertEqual("dummy", result)

if __name__ == '__main__':
    unittest.main()
