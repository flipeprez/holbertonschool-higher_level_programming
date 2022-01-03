#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        var = 0
        for j in i:
            if var != 0:
                print(" ", end='')
            print ("{:d}".format(j), end='')
            var += 1
        print()
