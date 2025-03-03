import psycopg2
import operations.cursor

class Writer:
    def __init__(self):
        pass

    def add_item(self, conn, item):
        cursor = operations.cursor.CursorManager().create_cursor(conn)

        try:
            cursor.execute("INSERT INTO inventory (name, count) VALUES('" + item.name + "', " + str(item.amount) + ");")
        except psycopg2.Error as err:
            print("Failed to write into inventory: " + str(err))
            raise
