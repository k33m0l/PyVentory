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
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("SQL version is ", record, "\n")