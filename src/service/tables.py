#!/usr/bin/env python3

import argparse
from operations.db_ops import create_table, delete_table, read_all_tables

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("-c", type=str, help="Sets mode to table creation. Table name must be provided.")
    modes.add_argument("-d", type=str, help="Sets mode to table deletion. Table name must be provided.")
    modes.add_argument("-l", action="store_true", help="Sets mode to table read")
    args = parser.parse_args()

    if args.c:
        create_table(args.c)
    elif args.d:
        delete_table(args.d)
    elif args.l:
        tables = read_all_tables()
        for table in tables:
            print(table)
    else:
        print("No valid parameters provided, please review your command")

