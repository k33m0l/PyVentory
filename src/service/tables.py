#!/usr/bin/env python3

import argparse
from operations.db_ops import create_table, delete_table, read_all_tables

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("-c", action="store_true", help="Sets mode to table creation")
    modes.add_argument("-d", action="store_true", help="Sets mode to table deletion")
    modes.add_argument("-l", action="store_true", help="Sets mode to table read")

    parser.add_argument("-t", type=str, help="Table name for create and delete modes")
    args = parser.parse_args()

    if args.c and args.t:
        create_table(args.t)
    elif args.d and args.t:
        delete_table(args.t)
    elif args.l:
        tables = read_all_tables()
        for table in tables:
            print(table)
    else:
        print("No valid parameters provided, please review your command")

