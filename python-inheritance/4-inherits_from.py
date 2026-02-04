#!/usr/bin/python3
"""
function that returns True if the object is an instance
"""


def inherits_from(obj, a_class):
    """
    inherits_from
    obj: object
    a_class: class
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
