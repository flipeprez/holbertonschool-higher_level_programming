#!/usr/bin/python3
'''comments'''


def appened_after(filename="", search_string="", new_string=""):
    '''comment'''
    with open(filename, encoding='utf-8') as f:
        aux = ""
        for line in f:
            aux += linea
            if search_string in linea:
                aux += new_string
        f.seek(0)
        f.write(aux)
