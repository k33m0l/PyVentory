import psycopg2
import os
import operations.cursor
import operations.reader
import operations.writer

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
        cursor.execute("CREATE TABLE inventory (name varchar(255), count int);")
    except psycopg2.Error as err:
        print("Failed to create database: " + str(err))
        raise

# Init DB
connection = connectToDB()
initDatabase(connection)

# Add sample data
db_writer = operations.writer.Writer()
db_writer.add_item(connection, "Mayo", 1)
db_writer.add_item(connection, "Cheese", 3)
db_writer.add_item(connection, "Salami", 4)

# Read all data from db
db_reader = operations.reader.Reader()
for item in db_reader.readAll(connection):
    print("Data from db: " + str(item))
