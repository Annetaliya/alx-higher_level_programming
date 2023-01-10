#!/usr/bin/python3
"""function that appends txt"""


def append_write(filename="", text=""):
    """ appended text"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
