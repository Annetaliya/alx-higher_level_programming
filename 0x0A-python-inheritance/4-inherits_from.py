#!/usr/bin/python3
"""Function that checks for instance of a class"""


def inherits_from(obj, a_class):
    """ Returns true is an instance of a class """

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
