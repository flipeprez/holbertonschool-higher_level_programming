#!/usr/bin/python3
'''comment'''


def add_attribute(cls, name, first):
    '''comment'''
    if not hasattr(cls, name):
        raise TypeError("cant't add new attribute")
    cls.name = first
