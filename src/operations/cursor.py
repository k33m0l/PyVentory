import psycopg2

class CursorManager:
    def create_cursor(self, conn):
        try:
            return conn.cursor()
        except psycopg2.Error as err:
            print("Failed to create database cursor: " + str(err))
            raise