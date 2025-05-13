import unittest
from unittest.mock import MagicMock
import src.service.items as under_test

SAMPLE_ITEM_1 = (1, "Item1", 10)
SAMPLE_ITEM_2 = (2, "Item2", 100)
SAMPLE_ITEM_3 = (3, "Item3", 3)

class ItemsTest(unittest.TestCase):

    def test_fetch_all(self):
        # GIVEN
        under_test.read_all_items = MagicMock(name="read_all_items")
        under_test.read_all_items.return_value = [SAMPLE_ITEM_1, SAMPLE_ITEM_2, SAMPLE_ITEM_3]

        # WHEN
        result = under_test.fetch_all()
        expected = [SAMPLE_ITEM_1, SAMPLE_ITEM_2, SAMPLE_ITEM_3]

        # THEN
        self.assertEqual(expected, result)
        under_test.read_all_items.assert_called_once()

if __name__ == '__main__':
    unittest.main()
