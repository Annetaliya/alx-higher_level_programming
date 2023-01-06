#!/usr/bin/python3
"""

This module has one function that adds up 2 integers

"""
 def add_integer(a, b=98):
     """Returns the sum of two integers

     Raises:
     TypeError if either of the args is not a float or integer
     """

     if ((not isinstance(a, int) and not isinstance(a, float))):
         raise TypeError("a must be an integer")
     if ((not isinstance(b, int) and not isinstance(b, float))):
         raise TypeError("b must be an integer")
     return (int(a) + int(b))
