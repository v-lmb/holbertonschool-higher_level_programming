#!/usr/bin/python3
"""
Python-test_driven_development.0-add_integer
"""
def add_integer(a, b=98):
    """
	Docstring pour add_integer
	
	:param a: int or float
	:param b: int or float
	"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
