#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    ks = []
    for k, valor in a_dictionary.items():
        if (valor == value):
            ks.append(k)
    for i in ks:
        del a_dictionary[i]
    return a_dictionary

