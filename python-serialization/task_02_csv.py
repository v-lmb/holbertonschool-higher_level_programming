#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, "r") as f:
            objt = csv.DictReader(f)
            with open("data.json", "w", encoding='utf-8') as file:
                json.dump(list(objt), file)
            return True
    except FileExistsError:
        return False
