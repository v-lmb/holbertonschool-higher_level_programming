#!/usr/bin/python3
"""
Create a class
"""


class BaseGeometry:
    """
    enpty class
    Raise: Exception
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
