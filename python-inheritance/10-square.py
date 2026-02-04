#!/usr/bin/python3
"""
Create a class
"""


class BaseGeometry:
    """
    BasGeometry class
    Raise: Exception, TypeError, ValueError
    """

    def __init__(self):
        pass

    def area(self):
        """
        area
        self: self
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator
        self: self
        name: string
        value: value
        """
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Rectangle class with parent BasGeometry
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        if type(self.__width) is not int or type(self.__height) is not int:
            raise TypeError(f"{self.name} must be an integer")
        if self.__width <= 0 or self.__height <= 0:
            raise ValueError(f"{self.name} must be greater than 0")

    def area(self):
        """
        area rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        __str__
        """
        return (f"[Rectangle] {self.__width}/{self.__height}")


class Square(Rectangle):
    """
    Square class with parent Rectangle
    """

    def __init__(self, size):
        self.__size = size

        self.integer_validator("size", self.__size)
        if type(self.__size) is not int:
            raise TypeError(f"{self.name} must be an integer")
        if self.__size <= 0:
            raise ValueError(f"{self.name} must be greater than 0")

    def area(self):
        """
        area square
        """
        return self.__size ** 2

    def __str__(self):
        """
        __str__
        """
        return (f"[Rectangle] {self.__size}/{self.__size}")
