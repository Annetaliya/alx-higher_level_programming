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

    def update(self, *args, **kwargs):
        """assigning of attributes"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]

        else:
            for k, v in kwargs.items():
                if k == "id":
                    if type(v) != int and v is not None:
                        raise TypeError('id must be an integer')
                    self.id = v
                if k == "size":
                    self.size = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def to_dictionary(self):
        """returns a dict rep of a Square"""
        sq_dic = {'id': self.id, 'size': self.size,
                  'x': self.x, 'y': self.y}

        return sq_dic
