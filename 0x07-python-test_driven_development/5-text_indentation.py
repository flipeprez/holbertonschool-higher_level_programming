#!/usr/bin/python3
'''comment'''


def text_indentation(text):
    '''comment'''
    buff = ""
    if not isintance(text, str):
        raise TypeError("text must be a string")
    for letra in text:
        buff += letra
        if letra == "." or letra == "?" or letra == ":":
            while buff[0] ==" ":
                buff = buff[1:]
                print(buff)
                print()
                buff = ""
        if len(buff) is not 0:
            try:
                while buff[0] == " ":
                    buff = buff[1:]
            except:
                pass
            print(buff)
