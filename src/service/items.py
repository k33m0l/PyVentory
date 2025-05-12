#!/usr/bin/env python3

from db_ops import connect_to_db
from operations.reader import Reader

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
