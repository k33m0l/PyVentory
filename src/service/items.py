#!/usr/bin/env python3

import argparse
from operations.db_ops import read_all_items, read_item_by_id, delete_item_by_id, add_item, update_item_by_id
from objects.item import Item

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("-c", type=str, help="Sets mode to item creation. Table name must be provided.")
    modes.add_argument("-d", type=str, help="Sets mode to item deletion. Table name must be provided.")
    modes.add_argument("-l", type=str, help="Sets mode to item read. Table name must be provided")

    parser.add_argument("-n", type=str, help="Name of the item")
    parser.add_argument("-a", type=int, help="Available amount of an item")
    parser.add_argument("-i", type=int, help="ID of an item in the database")
    args = parser.parse_args()

    if args.c and args.i and (args.n or args.a):
        update_item_by_id(args.c, args.i, name = args.n, count = args.a)
    elif args.c and args.n and args.a:
        add_item(args.c, Item(args.n, args.a))
    elif args.d and args.i:
        delete_item_by_id(args.d, args.i)
    elif args.l and args.i:
        result = read_item_by_id(args.l, args.i)
        print(result)
    elif args.l:
        result = read_all_items(args.l)
        for item in result:
            print(item)
    else:
        print("No valid parameters provided, please review your command")
