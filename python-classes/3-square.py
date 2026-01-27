#!/usr/bin/python3
"""
Create a square class
"""


class Square:
    """
    class for Square
    size: private instance attribute
    Return: square area
    Raise: ValueError, TypeError
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
