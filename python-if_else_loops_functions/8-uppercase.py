#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord(i) in range(97, 123)):
            print_char = chr(ord(i) - 32)
        else:
            print_char = i
        print(f"{print_char}".format(print_char), end='')
    print()
