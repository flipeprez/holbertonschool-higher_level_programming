#!/usr/bin/python3
'''lala'''


class Square:
    '''lalal'''
    def __init__(self, size=0):
        '''lala'''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    
    @property
    def size(self):
        '''lala'''
        return self.__size
    
    @size.setter
    def size(self, value):
        '''lala'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    def area(self):
        '''lala'''
        return self.__size * self.__size
