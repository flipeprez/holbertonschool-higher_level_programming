#!/usr/bin/python3
'''def class'''


class BaseGeometry:
    '''def subclass'''
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''def validator'''
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    '''def class'''

    def __init__(self, width, height):
        '''comment''' 
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
