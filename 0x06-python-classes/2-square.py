#!/usr/bin/python3
'''lalala'''


class Square:
'''lalala'''
    def __init__(self, size=0):
        '''lalala'''
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
