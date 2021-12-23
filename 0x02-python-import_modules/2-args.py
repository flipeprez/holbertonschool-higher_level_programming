#!/usr/bin/python3

from sys import argv


def argument():
    arg_str = "arguments"
    ifna = "."
    length = len(argv) - 1
    if (length == 1):
        arg_str = "argument"
    if (length - 1 >= 0):
        ifna = ":"
    print("{} {}{}".format(length, arg_str, ifna))

    for index, arg in enumerate(argv):
        if (index > 0):
            print("{}: {}".format(index, arg))


if __name__ == "__main__":
    argument()
