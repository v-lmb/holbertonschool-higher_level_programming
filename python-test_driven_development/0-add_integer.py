#!/usr/bin/python3
"""
Add two integers or floats and return an integer
"""


def add_integer(a, b=98):
    """
    Add two integers or floats and return an integer
    Parametres
    a : int or float
    b : int or float
    Return:
    int
    Raises:
    TypeError, OverflowError and ValueError
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
