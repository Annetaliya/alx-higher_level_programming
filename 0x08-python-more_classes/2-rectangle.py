#!/usr/bin/python3
"""Defines a class rectangle"""


class Rectangle:
    """ creates a class with instances"""

    def __init__(self, width=0, height=0):
        """ takes two args height and width """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """gets the width of rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('Width must be an integer')
        if value < 0:
            raise VlueError('width must be >= 0')
        self.__width = value

    @property
    def height(self, value):
        """ gets the height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """returns area of a rectangle"""

        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
