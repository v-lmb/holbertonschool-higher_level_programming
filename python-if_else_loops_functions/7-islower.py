#!/usr/bin/python3
#    return ord(c) <= 123 and ord(c) >= 97

def islower(c):
    if (ord(c) in range(97, 123)):
        return True
    else:
        return False
