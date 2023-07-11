#!/usr/bin/python3
"""script that adds all arguments to Python list, and save them to a file"""


import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        item_json = load_from_json_file("add_item.json")
    except FileNotFoundError:
        item_json = []
    item_json.extend(sys.argv[1:])
    save_to_json_file(item_json, "add_item.json")
