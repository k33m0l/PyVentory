import psycopg2
import operations.cursor

class Reader:
    def __init__(self):
        pass

    def read_all(self, conn):
        cursor = operations.cursor.CursorManager().create_cursor(conn)

        try:
            cursor.execute("SELECT * FROM inventory;")
            return cursor.fetchall()
        except psycopg2.Error as err:
            print("Failed to read from inventory: " + str(err))
            raise
