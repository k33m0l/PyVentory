import psycopg2
from db_ops import connect_to_db
from operations.writer import Writer
from objects.item import Item

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

    connection.close()

if __name__ == "__main__":
    init_application()
