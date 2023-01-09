#!/usr/bin/python3
""" Createing a subclass """


class MyList(list):
    """A subclass that inherits properties of the parent """

    def print_sorted(self):
        """A method that prints a sorted list"""

        print(sorted(self))
