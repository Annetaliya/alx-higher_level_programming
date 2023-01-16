#!/usr/bin/python3
from models.rectangle import Rectangle

""" declaration of a class"""


class Square(Rectangle):
    """class square that inherits from Recatangle"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """returns the size of a square"""
        return self.__width

    @size.setter
    def size(self, value):
        """updates the value of size"""
        if (type(value) is not int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value
        self.__height = value
