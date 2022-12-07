#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for key, value in (sorted(a_dictionary.items())):
        if a_dictionary == key:
            a_dictionary = value
        else:
            a_dictionary.update({})
    return (a_dictionary)
