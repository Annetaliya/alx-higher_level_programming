#!/usr/bin/python3
""" Creating an empty class"""


class BaseGeometry:
    """class with area calc method"""

    def area(self):
        """Method taht calc the ares"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
