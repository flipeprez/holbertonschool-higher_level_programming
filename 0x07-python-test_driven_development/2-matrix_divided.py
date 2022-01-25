#!/usr/bin/python3
'''
    doc
'''


def matrix_divided(matrix, div):
    '''
        matrix divided function
    '''
    nmatrix = []
    try:
        largo = len(matrix[0])
    except:
        pass
    error_list = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for fila in matrix:
        nfila = []
        if not isinstance(fila, list):
            raise TypeError(error_list)
        if largo != len(fila):
            raise TypeError("Each row must have the same size")
        for l in fila:
            if not isinstance(l, (int, float)):
                raise TypeError(error_list)
            resdiv = round(l / div, 2)
            nfila.append(resdiv)
        nmatrix.append(nfila)
    return nmatrix
