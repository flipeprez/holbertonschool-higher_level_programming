#!/usr/bin/python3
'''def class'''


class BaseGeometry:
    '''def subclass'''

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
        self.__width = width
        self.__height = height
        self.integer_validator("height", height)
        self.integer_validator("width", width)

    def area(self):
        '''def area'''
        return self.__width * self.__height

    def __str__(self):
        '''comment'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
