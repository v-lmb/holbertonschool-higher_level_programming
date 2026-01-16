#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    total = 0
    for valeur in argv[1:]:
        total = total + int(valeur)
    print(f"{total}")
