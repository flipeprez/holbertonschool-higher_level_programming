#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    nl = my_list.copy()
    if idx < 0:
        return nl
    if idx > len(my_list) - 1:
        return nl
    nl[idx] = element
    return nl
