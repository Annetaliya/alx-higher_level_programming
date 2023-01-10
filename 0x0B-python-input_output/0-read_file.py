#!/usr/bin/python3
"""function that raeds a file """


def read_file(filename=""):
    """prints content of a utf8 text file"""

    with open('my_file_0.txt', 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
