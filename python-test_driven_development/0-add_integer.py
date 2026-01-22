#!/usr/bin/python3
"""
Python-test_driven_development.0-add_integer
"""

def add_integer(a, b=98):
    """ Add two integers or floats and return an integer."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    try:
        a = int(a) or float(a)
    except (OverflowError):
        raise TypeError("a must be an integer")
    try:
        b = int(b) or float(b)
    except (OverflowError):
        raise TypeError("b must be an integer")

    return a + b
