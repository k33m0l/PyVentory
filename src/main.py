import psycopg2
import os
import operations.cursor
import operations.reader
import operations.writer
import objects.item

def connectToDB():
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
def initDatabase(conn):
    try:
        cursor = operations.cursor.CursorManager().create_cursor(conn)
        cursor.execute("CREATE TABLE IF NOT EXISTS inventory (name varchar(255), count int);")
    except psycopg2.Error as err:
        print("Failed to create database: " + str(err))
        raise

# Init DB
connection = connectToDB()
connection.autocommit = True
initDatabase(connection)

# Add sample data
data_1 = objects.item.Item("Mayo", 1)
data_2 = objects.item.Item("Cheese", 3)
data_3 = objects.item.Item("Salami", 4)

db_writer = operations.writer.Writer()
db_writer.add_item(connection, data_1)
db_writer.add_item(connection, data_2)
db_writer.add_item(connection, data_3)

# Read all data from db
db_reader = operations.reader.Reader()
for item in db_reader.read_all(connection):
    print("Data from db: " + str(item))
