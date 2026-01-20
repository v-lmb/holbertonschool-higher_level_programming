#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key, key_value in sorted(a_dictionary.items()):
        print(f"{key}: {key_value}")
