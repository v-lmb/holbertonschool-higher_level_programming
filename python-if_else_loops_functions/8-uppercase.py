#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord(i) in range(97, 123)):
            print_char = chr(ord(i) - 32)
        else:
            print_char = i
        print("{}".format(print_char), end='')
    print()
