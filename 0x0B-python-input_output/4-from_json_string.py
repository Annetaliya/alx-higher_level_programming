#!/usr/bin/python3
"""importing a module """
import json


def from_json_string(my_str):
    """function that returns a string as an object"""

    return json.loads(my_str)
