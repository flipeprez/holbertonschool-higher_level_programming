#!/usr/bin/python3
'''lalala'''


class Square:
    '''lalal'''
    def __init__(self, size=0,):
        '''lalal'''
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''lala'''
        return self.__size * self.__size
