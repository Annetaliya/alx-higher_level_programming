#!/usr/bin/python3
"""class declaration """


class Student:
    """class student declared """

    def __init__(self, first_name, last_name, age):
        """initialization of public attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method that return a dictionary rep of class student"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs
                    if hasattr(self, k)}
        return self.__dict__
