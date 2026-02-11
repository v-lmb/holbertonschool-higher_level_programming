#!/usr/bin/python3
"""
0-read_file
"""


def read_file(filename=""):
    """
    read_file
    filename: as it's write
    """
    with open(filename, "r", encoding='utf-8') as f:
        return f.read()
