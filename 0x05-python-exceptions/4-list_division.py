#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nlist = []
    indx = 0
    if list_length <= 0:
        print("out of range")
        return nlist
    while indx < list_length:
        try:
            nlist.append(my_list_1[indx] / my_list_2[indx])
        except TypeError:
            print("wrong type")
            nlist.append(0)
        except ZeroDivisionError:
            print("division by 0")
            nlist.append(0)
        except IndexError:
            print("out of range")
            nlist.append(0)
        finally:
            indx += 1
    return nlist
