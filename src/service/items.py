#!/usr/bin/env python3

from db_ops import connect_to_db
from operations.reader import Reader

def fetch_all(connection):
    db_reader = Reader()
    return db_reader.read_all(connection)

def run():
    conn = connect_to_db()
    response = fetch_all(conn)
    conn.close()
    return response

if __name__ == "__main__":
    # input will go here
    response = run()
    for item in response:
        print("Data from db: " + str(item))
