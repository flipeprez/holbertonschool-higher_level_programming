#!/usr/bin/python3
'''comment'''


def read_file(filename=""):
    '''comment'''
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
