#!/usr/bin/python3
'''class comments'''


class Rectangle:
    '''define rectangle class'''
    def __init__(self, width=0, height=0):
        '''def func'''
        self.width = width
        self.height = height

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

    def area(self):
        '''define area self'''
        return self.height * self.width

    def perimeter(self):
        '''define perimeter'''
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2
