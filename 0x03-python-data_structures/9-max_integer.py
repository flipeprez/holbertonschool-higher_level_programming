#!/usr/bin/python3
def max_integer(my_list=[]):
    bigger = -999999
    if len(my_list) == 0:
        return (None)
    for i in my_list:
        if i > bigger:
            bigger = i
    return (bigger)
