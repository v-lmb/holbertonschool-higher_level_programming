#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """
    serialize_and_save_to_file
    data: A Python Dictionary with data
    filename: The filename of the output JSON file.
    If the output file already exists it should be replaced.
    """
    with open(filename, "w") as f:
        f.write(json.dump(data))


def load_and_deserialize(filename):
    """
    load_and_deserialize
    filename: The filename of the input JSON file This function returns
    a Python Dictionary with the deseialized JSON data from the file.
    """
    with open(filename, "r") as f:
        return json.load(f.read())
