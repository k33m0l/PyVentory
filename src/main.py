import psycopg2

connection = psycopg2.connect(
    database="pyventory",
    host="database",
    user="admin",
    password="12345",
    port="5432"
)

cursor = connection.cursor()
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("SQL version is ", record, "\n")