#!/usr/bin/python3
"""function declaration"""


def class_to_json(obj):
    """returns a dict description with simple data structure"""

    my_dict = {}
    for key, value in obj.__dict__.items():
        my_dict = value
    return my_dict
