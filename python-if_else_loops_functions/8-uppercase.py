#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord(i) in range(97, 123)):
            prnt_char = chr(ord(i) - 32)
        else:
            prnt_char = i
        print("{}".format(prnt_char), end='')
    print()
