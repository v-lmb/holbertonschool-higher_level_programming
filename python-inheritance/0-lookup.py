#!/usr/bin/python3
"""
Returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    lookup
    obj: object
    Return: list of attributes and methods of objects
    """
    return dir(obj)
