#!/usr/bin/python3
def element_at(my_list, idx):
    for inx in my_list[0:]:
        if my_list[idx] < 0 or my_list[idx] > len(my_list):
            return None
        else:
            return my_list[idx]
