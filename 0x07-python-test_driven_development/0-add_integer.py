#!/usr/bin/python3
def add_integer(a, b=98):
    '''add integer function'''
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be a integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be a integer")
    return int(a + b)
