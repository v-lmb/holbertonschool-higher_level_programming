#!/usr/bin/python3
"""
Create object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    load_from_json_file
    filename: filename
    """
    with open(filename, "r") as f:
        return json.loads(f.read())
