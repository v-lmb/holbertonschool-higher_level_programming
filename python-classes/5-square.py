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
        area of Square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        get size Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set size Square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        print square with #
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print('#' * self.__size)
