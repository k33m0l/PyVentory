#!/usr/bin/env python3

import psycopg2
import os
from operations.reader import Reader

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

def fetch_all(connection):
    # Read all data from db
    db_reader = Reader()
    for item in db_reader.read_all(connection):
        print("Data from db: " + str(item))

def run():
    conn = connect_to_db()
    fetch_all(conn)
    conn.close()

if __name__ == "__main__":
    run()
