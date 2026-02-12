#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """
    serialize_and_save_to_file
    """
    with open(filename, "w") as f:
        f.write(json.dumps(data))


def load_and_deserialize(filename):
    """
    load_and_deserialize
    """
    with open(filename, "r") as f:
        return json.loads(f.read())
