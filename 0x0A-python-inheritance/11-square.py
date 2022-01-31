#!/usr/bin/python3


Rectangle = __import__('9-rectangle').Rectangle
'''comment'''


class Square(Rectangle):
    '''comment'''
    def __init__(self, size):
        '''comment'''
        self.__size = size
        self.integer_validator('size', size)
        super().__init__(size, size)

    def __str__(self):
        '''comment'''
        return "[Square] {}/{}".format(self.__size, self.__size)
