#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    convert_csv_to_json
    """
    try:
        with open(csv_filename, "r") as f:
            reader = csv.DictReader(f)
            data = list(reader)
            with open("data.json", "w", encoding='utf-8') as file:
                json.dump(data, file)
            return True
    except FileExistsError:
        return False
