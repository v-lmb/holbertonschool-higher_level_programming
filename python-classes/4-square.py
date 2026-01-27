#!/usr/bin/python3
"""
Create a square class
"""


class Square:
    """
    class for Square
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        class for area of Square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        class for get size Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        class for set size Square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
