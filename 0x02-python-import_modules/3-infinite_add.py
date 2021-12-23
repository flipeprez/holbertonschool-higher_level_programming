#!/usr/bin/python3
from sys import argv


def add_all():
    sum = 0

    for i, number in enumerate(argv):
        if (i > 0):
            sum = sum + int(number)
    print("{:d}".format(sum))

    if __name__ == "__main__":
        add_all()
