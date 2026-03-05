#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, "r", newline='') as f:
            objt = csv.DictReader(f)
            data = list(objt)
        with open("data.json", "w", encoding='utf-8') as file:
            json.dump(data, file)
        return True
    except FileExistsError:
        return False
