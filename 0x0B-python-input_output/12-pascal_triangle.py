#!/usr/bin/python3
'''comment'''


def pascal_triangle(n):
    '''comment'''
    matrix = []
    for fila in range(n):
        tmp = [0] * (fila + 1)
        tmp[0] = 1
        tmp[fila] = 1
        if fila > 1:
            tmp[1] = fila
            tmp[fila - 1] = fila
        while 0 in tmp:
            indx = tmp.index(0)
            num = matrix[fila - 1][indx] + matrix[fila - 1][indx - 1]
            tmp[indx] = num
        matrix.append(tmp)
    return matrix
