#!/usr/bin/python3
"""
Write a class MyList that inherits from list:
Public instance method: def print_sorted(self)
You can assume that all the elements of the list will be of type int
You are not allowed to import any module
"""


class MyList(list):
    """
    MyList
    """
    def __init__(self):
        pass

    def print_sorted(self):
        """
        print_sorted
        self: self
        """
        print(sorted(self))
