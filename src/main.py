import psycopg2
import os
from operations.reader import Reader
from operations.writer import Writer
from objects.item import Item

def connect_to_db():
    try:
        return psycopg2.connect(
            database=os.environ["DB_NAME"],
            host="database",
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASS"],
            port="5432"
        )
    except psycopg2.Error as err:
        print("Error connecting to database: " + str(err))
        raise

# Create table
def init_db(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS inventory (name varchar(255), count int);")
    except psycopg2.Error as err:
        print("Failed to create database: " + str(err))
        raise

def init_application():
    # Init DB
    connection = connect_to_db()
    connection.autocommit = True
    init_db(connection)

    # Add sample data
    data_1 = Item("Mayo", 1)
    data_2 = Item("Cheese", 3)
    data_3 = Item("Salami", 4)

    db_writer = Writer()
    db_writer.add_item(connection, data_1)
    db_writer.add_item(connection, data_2)
    db_writer.add_item(connection, data_3)

    # Read all data from db
    db_reader = Reader()
    for item in db_reader.read_all(connection):
        print("Data from db: " + str(item))

if __name__ == "__main__":
    init_application()
