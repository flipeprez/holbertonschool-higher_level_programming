#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dictionary = {}
    for key, val in a_dictionary.items():
        n_dictionary.update({key: val * 2})
    return n_dictionary

