#!/usr/bin/python3
""" class defined """


class Square:
    """ class square declared """

    def __init__(self, size=0):
        """ method takes two args size
            should be an integer and > 0
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Calculates the area of a square
        Returns: the square of the size
        """

        return (self.__size ** 2)
