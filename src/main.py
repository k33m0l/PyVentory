import psycopg2
import os


connection = psycopg2.connect(
    database=os.environ["DB_NAME"],
    host="database",
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASS"],
    port="5432"
)

cursor = connection.cursor()

# Create table
cursor.execute("CREATE TABLE inventory (name varchar(255), count int);")

# Add example data
cursor.execute("INSERT INTO inventory (name, count) VALUES('Mayo', 1);")
cursor.execute("INSERT INTO inventory (name, count) VALUES('Cheese', 3);")
cursor.execute("INSERT INTO inventory (name, count) VALUES('Salami', 4);")

# Query all data
cursor.execute("SELECT * FROM inventory;")


record = cursor.fetchall()

for item in record:
    print("Data from db: " + str(item))
