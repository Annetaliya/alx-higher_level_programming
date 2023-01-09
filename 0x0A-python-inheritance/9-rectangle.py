#!/usr/bin/python3
"""inherits from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A claas that inherits the parent class"""

    def __init__(self, width, height):
        """initializes a new rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calc area of a rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """prints obj to stdout"""

        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
