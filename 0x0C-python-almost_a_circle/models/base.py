#!/usr/bin/python3
"""Class declaration """


class Base:
    """A class that defines objects """
    __nb_objects = 0

    def __init__(self, id=None):
        """instasiation of objects with attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
