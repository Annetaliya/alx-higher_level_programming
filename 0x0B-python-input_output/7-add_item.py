#!/usr/bin/python3
"""this module adds all args to python list and saves in afile """


import sys

if __name__ == "__main__":

    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
        items.extend(sys.argv[1:])
        save_to_jsonfile(items, "add_item.json")
