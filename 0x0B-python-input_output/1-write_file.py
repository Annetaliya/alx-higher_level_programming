#!/usr/bin/python3
""" function that writes to stdout"""


def write_file(filename="", text=""):
    """overwrites a text file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
