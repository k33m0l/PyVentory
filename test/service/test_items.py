import unittest
from unittest.mock import MagicMock, patch
import src.service.items as under_test

class ItemsTest(unittest.TestCase):

    @patch("src.service.items.Reader")
    def test_fetch_all(self, reader_mock_class):
        under_test.connect_to_db = MagicMock(name="connect_to_db")
        mock_conn = MagicMock()
        under_test.connect_to_db.return_value = mock_conn

        reader_mock = reader_mock_class.return_value
        reader_mock.conn = mock_conn
        reader_mock.read_all.return_value = ["asd", "dsa"]

        result = under_test.run()
        self.assertEqual(["asd", "dsa"], result)

if __name__ == '__main__':
    unittest.main()
