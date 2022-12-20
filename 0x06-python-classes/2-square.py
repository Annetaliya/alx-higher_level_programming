#!/usr/bin/python3
""" Class square defined """


class Square:
    """ class that has one object """

    def __init__(self, size=0):
        """ method that refers to an object
        Args:
            size: represents the size of the square defined
        Raises:
            typeError: if size is not an integer
            ValueError: if size is less than zero
            """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
