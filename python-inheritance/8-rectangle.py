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
        if type(self.__width) is not int:
            raise TypeError(f"{self.name} must be an integer")
        if self.__width <= 0:
            raise ValueError(f"{self.name} must be greater than 0")

        self.integer_validator("height", height)
        if type(self.__height) is not int:
            raise TypeError(f"{self.name} must be an integer")
        if self.__height <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
