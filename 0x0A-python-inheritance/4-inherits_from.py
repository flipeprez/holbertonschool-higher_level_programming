#!/usr/bin/python3
'''comments'''


def inherits_from(obj, a_class):
    if type(obj) == a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
