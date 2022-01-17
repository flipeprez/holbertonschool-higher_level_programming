#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    indx = 0
    try:
        for item in range(0, x):
            print("{}".format(my_list[item]), end="")
            indx +=1
    except IndexError:
        pass
    print()
    return indx
