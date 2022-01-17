#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    indx = 0
    
    for indx in range(x):
        try:
            print("{:d}".format[indx], end="")
            indx += 1
        except (TypeError, ValueError):
            pass
    print()
    return indx
