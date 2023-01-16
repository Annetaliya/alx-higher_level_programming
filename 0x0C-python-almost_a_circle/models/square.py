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
