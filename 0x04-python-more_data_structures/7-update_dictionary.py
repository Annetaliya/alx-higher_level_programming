#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for key, value in (sorted(a_dictionary.items())):
        if a_dictionary == key:
            a_dictionary = value
    return (a_dictionary)
