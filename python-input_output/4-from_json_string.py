#!/usr/bin/python3
"""
from json string to object
"""
import json


def from_json_string(my_str):
    """
    from_json_string
    my_str: strings
    """
    return json.loads(my_str)
