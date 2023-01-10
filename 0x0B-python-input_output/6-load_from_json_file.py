#!/usr/bin/python3
"""importing a module """
import json


def load_from_json_file(filename):
    """craetes an object from a json file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
