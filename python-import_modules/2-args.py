#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print(f"{len(argv) - 1} argument:".format(len(argv)))
        print(f"{argv}: {argv}".format(len(argv)))

    elif len(argv) > 1:
        print(f"{len(argv) - 1} arguments:".format(len(argv)))
        for i in range(1, len(argv)):
            print(f"{i}: {argv[i]}".format(argv))

    else:
        print(f"{len(argv)} arguments.".format(len(argv)))
