#!/usr/bin/env python3

import argparse
from db_ops import connect_to_db
from operations.reader import Reader

def fetch_all():
    conn = connect_to_db()
    db_reader = Reader()
    response = db_reader.read_all(conn)
    conn.close()
    return response

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", action="store_true", help="Example flag used for testing")
    args = parser.parse_args()

    if args.e:
        print("Flag was set!")

    # input will go here
    response = fetch_all()
    for item in response:
        print("Data from db: " + str(item))
