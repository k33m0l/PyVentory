import unittest
from unittest.mock import MagicMock, patch
from src.objects.item import Item
import src.operations.db_ops as under_test

SAMPLE_ITEM_1 = (1, "Item1", 10)
SAMPLE_ITEM_2 = (2, "Item2", 100)
SAMPLE_ITEM_3 = (3, "Item3", 3)
ITEM_WITHOUT_ID = Item("NewItem", 20)
OS_ENVIRON = {
    "DB_NAME": "temp",
    "DB_USER": "tempuser",
    "DB_PASS": "temppass",
}

class ItemsTest(unittest.TestCase):

    @patch.dict("os.environ", OS_ENVIRON, clear=True)
    def test_connect_to_db(self):
        # GIVEN
        expected_conn = MagicMock()
        under_test.psycopg2.connect = MagicMock()
        under_test.psycopg2.connect.return_value = expected_conn
        
        # WHEN
        result = under_test.connect_to_db()
        
        # THEN
        self.assertTrue(result.autocommit)
        self.assertEqual(expected_conn, result)
        under_test.psycopg2.connect.assert_called_once()

    @patch("src.operations.db_ops.connect_to_db")
    @patch("src.operations.db_ops.psycopg2.sql.SQL")
    @patch("src.operations.db_ops.psycopg2.sql.Identifier")
    def test_create_table(self, mock_identifier_class, mock_sql_class, mock_connect_to_db):
        # GIVEN
        expected_query = "something something testdbname"
        mock_conn = MagicMock()
        mock_connect_to_db.return_value = mock_conn
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_sql = mock_sql_class.return_value
        mock_sql.format.return_value = expected_query
        mock_identifier = mock_identifier_class.return_value
        
        # WHEN
        under_test.create_table("testdbname")
        
        # THEN
        mock_connect_to_db.assert_called_once()
        mock_conn.cursor.assert_called_once()
        mock_sql.format.assert_called_once_with(mock_identifier)
        mock_cursor.execute.assert_called_once_with(expected_query)
        mock_conn.close.assert_called_once()

    @patch("src.operations.db_ops.connect_to_db")
    @patch("src.operations.db_ops.psycopg2.sql.SQL")
    @patch("src.operations.db_ops.psycopg2.sql.Identifier")
    def test_delete_table(self, mock_identifier_class, mock_sql_class, mock_connect_to_db):
        # GIVEN
        expected_query = "something something testdbname"
        mock_conn = MagicMock()
        mock_connect_to_db.return_value = mock_conn
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_sql = mock_sql_class.return_value
        mock_sql.format.return_value = expected_query
        mock_identifier = mock_identifier_class.return_value
        
        # WHEN
        under_test.delete_table("testdbname")
        
        # THEN
        mock_connect_to_db.assert_called_once()
        mock_conn.cursor.assert_called_once()
        mock_sql.format.assert_called_once_with(mock_identifier)
        mock_cursor.execute.assert_called_once_with(expected_query)
        mock_conn.close.assert_called_once()

    @patch("src.operations.db_ops.connect_to_db")
    def test_read_all_items(self, mock_connect_to_db):
        # GIVEN
        mock_conn = MagicMock()
        mock_connect_to_db.return_value = mock_conn
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [SAMPLE_ITEM_1, SAMPLE_ITEM_2, SAMPLE_ITEM_3]

        expected = [SAMPLE_ITEM_1, SAMPLE_ITEM_2, SAMPLE_ITEM_3]
        
        # WHEN
        result = under_test.read_all_items()
        
        # THEN
        self.assertEqual(expected, result)
        mock_connect_to_db.assert_called_once()
        mock_conn.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT * FROM inventory;")
        mock_cursor.fetchall.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch("src.operations.db_ops.connect_to_db")
    def test_add_item(self, mock_connect_to_db):
        # GIVEN
        mock_conn = MagicMock()
        mock_connect_to_db.return_value = mock_conn
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        
        # WHEN
        under_test.add_item(ITEM_WITHOUT_ID)

        # THEN
        mock_connect_to_db.assert_called_once()
        mock_conn.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO inventory (name, count) VALUES(%(item_name)s, %(item_amount)s);",
            {
                "item_name": ITEM_WITHOUT_ID.name,
                "item_amount": str(ITEM_WITHOUT_ID.amount),
            }
        )
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
