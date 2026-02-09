#!/usr/bin/python3
"""
1-write_file
"""


def write_file(filename="", text=""):
    """
    write_file
    filename: File Name
    text: text to add
    """
    with open("my_first_file.txt", "w") as f:
        return f.write(text)
