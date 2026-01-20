#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    one = set_1 - set_2
    two = set_2 - set_1
    return (two.union(one))
