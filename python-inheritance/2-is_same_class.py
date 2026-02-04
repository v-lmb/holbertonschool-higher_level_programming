#!/usr/bin/python3
"""
function that returns True
if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    class for Rectangle
    obj: width of rectangle
    a_class: height of rectangle
    Return: True if is exactly the specified class
    """
    if isinstance(type(obj), a_class):
        return True
