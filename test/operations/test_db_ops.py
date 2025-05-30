import re
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
    def test_read_all_tables(self, mock_connect_to_db):
        # GIVEN
        mock_conn = MagicMock()
        mock_connect_to_db.return_value = mock_conn
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = ["testdbname", "anotherdb"]

        expected = ["testdbname", "anotherdb"]
        
        # WHEN
        result = under_test.read_all_tables()
        
        # THEN
        self.assertEqual(expected, result)
        mock_connect_to_db.assert_called_once()
        mock_conn.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
        mock_cursor.fetchall.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch("src.operations.db_ops.connect_to_db")
    @patch("src.operations.db_ops.psycopg2.sql.SQL")
    @patch("src.operations.db_ops.psycopg2.sql.Identifier")
    def test_read_all_items(self, mock_identifier_class, mock_sql_class, mock_connect_to_db):
        # GIVEN
        expected_query = "SELECT * FROM testdbname;"
        mock_conn = MagicMock()
        mock_connect_to_db.return_value = mock_conn
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_sql = mock_sql_class.return_value
        mock_sql.format.return_value = expected_query
        mock_identifier = mock_identifier_class.return_value
        mock_cursor.fetchall.return_value = [SAMPLE_ITEM_1, SAMPLE_ITEM_2, SAMPLE_ITEM_3]

        expected = [SAMPLE_ITEM_1, SAMPLE_ITEM_2, SAMPLE_ITEM_3]
        
        # WHEN
        result = under_test.read_all_items("testdbname")
        
        # THEN
        self.assertEqual(expected, result)
        mock_connect_to_db.assert_called_once()
        mock_conn.cursor.assert_called_once()
        mock_sql.format.assert_called_once_with(mock_identifier)
        mock_cursor.execute.assert_called_once_with(expected_query)
        mock_cursor.fetchall.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch("src.operations.db_ops.connect_to_db")
    @patch("src.operations.db_ops.psycopg2.sql.SQL")
    @patch("src.operations.db_ops.psycopg2.sql.Identifier")
    def test_read_item_by_id(self, mock_identifier_class, mock_sql_class, mock_connect_to_db):
        # GIVEN
        expected_query = "SELECT * FROM testdbname WHERE item_id = %s;"
        mock_conn = MagicMock()
        mock_connect_to_db.return_value = mock_conn
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_sql = mock_sql_class.return_value
        mock_sql.format.return_value = expected_query
        mock_identifier = mock_identifier_class.return_value
        mock_cursor.fetchone.return_value = SAMPLE_ITEM_1

        # WHEN
        result = under_test.read_item_by_id("testdbname", 1)
        
        # THEN
        self.assertEqual(SAMPLE_ITEM_1, result)
        mock_connect_to_db.assert_called_once()
        mock_conn.cursor.assert_called_once()
        mock_sql.format.assert_called_once_with(
            table=mock_identifier,
        )
        mock_cursor.execute.assert_called_once_with(expected_query, [1])
        mock_cursor.fetchone.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch("src.operations.db_ops.connect_to_db")
    @patch("src.operations.db_ops.psycopg2.sql.SQL")
    @patch("src.operations.db_ops.psycopg2.sql.Identifier")
    def test_delete_item_by_id(self, mock_identifier_class, mock_sql_class, mock_connect_to_db):
        # GIVEN
        expected_query = "DELETE FROM testdbname WHERE item_id = %s"
        mock_conn = MagicMock()
        mock_connect_to_db.return_value = mock_conn
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_sql = mock_sql_class.return_value
        mock_sql.format.return_value = expected_query
        mock_identifier = mock_identifier_class.return_value
        
        # WHEN
        under_test.delete_item_by_id("testdbname", 1)
        
        # THEN
        mock_connect_to_db.assert_called_once()
        mock_conn.cursor.assert_called_once()
        mock_sql.format.assert_called_once_with(
            table=mock_identifier,
        )
        mock_cursor.execute.assert_called_once_with(expected_query, [1])
        mock_conn.close.assert_called_once()

    @patch("src.operations.db_ops.connect_to_db")
    @patch("src.operations.db_ops.psycopg2.sql.SQL")
    @patch("src.operations.db_ops.psycopg2.sql.Identifier")
    @patch("src.operations.db_ops.psycopg2.sql.Composed")
    def test_update_item_by_id(self, mock_composed_class, mock_identifier_class, mock_sql_class, mock_connect_to_db):
        # GIVEN
        expected_query = "UPDATE testdbname SET name = %s, count = %s WHERE item_id = %s;"
        mock_conn = MagicMock()
        mock_connect_to_db.return_value = mock_conn
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_sql = mock_sql_class.return_value
        mock_composed = mock_composed_class.return_value
        mock_sql.join.return_value = mock_composed
        mock_sql.format.return_value = expected_query
        mock_identifier = mock_identifier_class.return_value
        
        # WHEN
        under_test.update_item_by_id("testdbname", 1, name = "New name", count = 5)
        
        # THEN
        mock_connect_to_db.assert_called_once()
        mock_conn.cursor.assert_called_once()
        mock_sql.format.assert_called_once_with(
            table=mock_identifier,
            update_variables=mock_composed
        )
        mock_cursor.execute.assert_called_once_with(expected_query, ["New name", 5, 1])
        mock_conn.close.assert_called_once()

    @patch("src.operations.db_ops.connect_to_db")
    @patch("src.operations.db_ops.psycopg2.sql.SQL")
    @patch("src.operations.db_ops.psycopg2.sql.Identifier")
    @patch("src.operations.db_ops.psycopg2.sql.Composed")
    def test_update_item_by_id_with_not_all_fields_provided(self, mock_composed_class, mock_identifier_class, mock_sql_class, mock_connect_to_db):
        # GIVEN
        expected_query = "UPDATE testdbname SET count = %s WHERE item_id = %s;"
        mock_conn = MagicMock()
        mock_connect_to_db.return_value = mock_conn
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_sql = mock_sql_class.return_value
        mock_composed = mock_composed_class.return_value
        mock_sql.join.return_value = mock_composed
        mock_sql.format.return_value = expected_query
        mock_identifier = mock_identifier_class.return_value
        
        # WHEN
        under_test.update_item_by_id("testdbname", 1, count = 10)
        
        # THEN
        mock_connect_to_db.assert_called_once()
        mock_conn.cursor.assert_called_once()
        mock_sql.format.assert_called_once_with(
            table=mock_identifier,
            update_variables=mock_composed
        )
        mock_cursor.execute.assert_called_once_with(expected_query, [10, 1])
        mock_conn.close.assert_called_once()

    @patch("src.operations.db_ops.connect_to_db")
    @patch("src.operations.db_ops.psycopg2.sql.SQL")
    @patch("src.operations.db_ops.psycopg2.sql.Identifier")
    def test_add_item(self, mock_identifier_class, mock_sql_class, mock_connect_to_db):
        # GIVEN
        expected_query = f"INSERT INTO testdbname (name, count) VALUES(%s, %s);"
        mock_conn = MagicMock()
        mock_connect_to_db.return_value = mock_conn
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_sql = mock_sql_class.return_value
        mock_sql.format.return_value = expected_query
        mock_identifier = mock_identifier_class.return_value
        
        # WHEN
        under_test.add_item("testdbname", ITEM_WITHOUT_ID)

        # THEN
        mock_connect_to_db.assert_called_once()
        mock_conn.cursor.assert_called_once()
        mock_sql.format.assert_called_once_with(
            table=mock_identifier,
        )
        mock_cursor.execute.assert_called_once_with(expected_query, (ITEM_WITHOUT_ID.name, ITEM_WITHOUT_ID.amount))
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
