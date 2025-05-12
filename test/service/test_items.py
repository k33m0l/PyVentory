import unittest
from unittest.mock import MagicMock, patch
import src.service.items as under_test

SAMPLE_ITEM_1 = (1, "Item1", 10)
SAMPLE_ITEM_2 = (2, "Item2", 100)
SAMPLE_ITEM_3 = (3, "Item3", 3)

class ItemsTest(unittest.TestCase):

    @patch("src.service.items.Reader")
    def test_fetch_all(self, reader_mock_class):
        # GIVEN
        under_test.connect_to_db = MagicMock(name="connect_to_db")
        mock_conn = MagicMock()
        under_test.connect_to_db.return_value = mock_conn

        reader_mock = reader_mock_class.return_value
        reader_mock.conn = mock_conn
        reader_mock.read_all.return_value = [SAMPLE_ITEM_1, SAMPLE_ITEM_2, SAMPLE_ITEM_3]

        # WHEN
        result = under_test.fetch_all()
        expected = [SAMPLE_ITEM_1, SAMPLE_ITEM_2, SAMPLE_ITEM_3]

        # THEN
        self.assertEqual(expected, result)
        under_test.connect_to_db.assert_called_once()
        reader_mock.read_all.assert_called_once_with(mock_conn)

if __name__ == '__main__':
    unittest.main()
