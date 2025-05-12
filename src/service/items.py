#!/usr/bin/env python3

from db_ops import connect_to_db
from operations.reader import Reader

def fetch_all():
    conn = connect_to_db()
    db_reader = Reader()
    response = db_reader.read_all(conn)
    conn.close()
    return response

if __name__ == "__main__":
    # input will go here
    response = fetch_all()
    for item in response:
        print("Data from db: " + str(item))
