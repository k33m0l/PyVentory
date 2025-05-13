#!/usr/bin/env python3

import argparse
from operations.db_ops import read_all_items

def fetch_all():
    return read_all_items("inventory")

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
