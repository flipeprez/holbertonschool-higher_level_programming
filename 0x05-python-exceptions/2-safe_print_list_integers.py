#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    indx = 0

    for item in range(x):
        try:
            print("{:d}".format(my_list[item]), end="")
            indx += 1
        except (TypeError, ValueError):
            pass
    print()
    return indx
