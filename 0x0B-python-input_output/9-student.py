#!/usr/bin/python3
"""creating a class student"""


class Student:
    """class student created with public attributes """

    def __init__(self, first_name, last_name, age):
        """" initialization of public attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """gets a dictionary representation of the student"""
        return self.__dict__
