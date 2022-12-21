#!/usr/bin/python3
"""A module that defines a square"""


class Square:
    """Reprseents a square with a size."""

    def __init__(self, size=0):
        """initializes the data """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Retrives size of sqaure"""

        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        calculates the ares of a square
        Returns: the sqaure of the size
        """

        return (self.__size ** 2)
