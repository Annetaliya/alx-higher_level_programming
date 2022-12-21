#!/usr/bin/python3
"""declaration of a class """


class Square:
    """initializing a class with size instance"""

    def __init__(self, size=0):
        """A method with two args"""

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
    @property
    def size(self):
        """Returs the instance size """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """calculates the area of sqaure"""

        return (self.__size ** 2)

    def my_print(self):
        """prints athe square with the character #"""
        if self.__size == 0:
            print()

        for i in range(self.__size):
             print("#" * self.__size)
