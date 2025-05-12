import psycopg2
import os

def connect_to_db():
    try:
        conn = psycopg2.connect(
            database=os.environ["DB_NAME"],
            host="database",
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASS"],
            port="5432"
        )
        conn.autocommit = True
        return conn
    except psycopg2.Error as err:
        print("Error connecting to database: " + str(err))
        raise
