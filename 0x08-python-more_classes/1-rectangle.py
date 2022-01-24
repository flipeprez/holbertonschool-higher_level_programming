#!/usr/bin/python3
'''class comment'''


class Rectangle:
    '''define rectangle class'''
    def __init__(self, width=0, height=0):
        '''def func'''
        self.height = height
        self.width = width

    @property
    def width(self):
        '''define property'''
        return self.__width

    @width.setter
    def width(self, value):
        '''define width setter'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''define prperty'''
        return self.__height

    @height.setter
    def height(self, value):
        '''define height setter'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
