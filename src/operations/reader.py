import psycopg2

class Reader:
    def __init__(self):
        pass

    def read_all(self, conn):
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM inventory;")
            return cursor.fetchall()
        except psycopg2.Error as err:
            print("Failed to read from inventory: " + str(err))
            raise

