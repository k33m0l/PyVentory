class Reader:
    def readAll(self, conn):
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM inventory;")
        return cursor.fetchall()