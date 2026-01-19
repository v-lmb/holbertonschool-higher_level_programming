#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list = my_list
    for i in list[::-1]:
        print("{:d}".format(i))
