import operations.cursor

class Reader:
    def __init__(self):
        pass

    def readAll(self, conn):
        cursor = operations.cursor.CursorManager().create_cursor(conn)

        cursor.execute("SELECT * FROM inventory;")
        return cursor.fetchall()
