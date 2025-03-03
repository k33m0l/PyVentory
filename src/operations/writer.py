import operations.cursor

class Writer:
    def __init__(self):
        pass

    def add_item(self, conn, item):
        cursor = operations.cursor.CursorManager().create_cursor(conn)

        cursor.execute("INSERT INTO inventory (name, count) VALUES('" + item.name + "', " + str(item.amount) + ");")
