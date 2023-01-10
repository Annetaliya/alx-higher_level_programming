#!/usr/bin/python3
"""importing a module"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a txt file using json format"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
