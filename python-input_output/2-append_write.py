#!/usr/bin/python3
"""
append file
"""


def append_write(filename="", text=""):
    """
    append_write
    filename: File Name
    text: text to add
    """
    with open("my_first_file.txt", "a") as f:
        return f.write(text)
