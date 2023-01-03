#!/usr/bin/python3
""" Defines a class Rectangle """


class Rectangle:
    """ creates a class with attributes """

    def __init__(self, width=0, height=0):
        """ Initializes the data """

        if not isinstance(width, int):

            raise TypeError('size must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrives size of rectangel"""

        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Retrives height of rectangle"""

        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError(' size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__height = value
