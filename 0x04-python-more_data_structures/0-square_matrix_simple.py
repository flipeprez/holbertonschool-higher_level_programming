#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_ma = []
    for i in matrix:
        new_ma.append(list(map(lambda sq: sq * sq, i)))
    return (new_ma)
