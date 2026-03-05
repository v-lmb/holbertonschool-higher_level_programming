#!/usr/bin/python3

'''
module for function that append string in text
'''


from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    List = load_from_json_file("add_item.json")
except FileNotFoundError:
    List = []
for i in argv[1:]:
    List.append(i)
save_to_json_file(List, "add_item.json")
