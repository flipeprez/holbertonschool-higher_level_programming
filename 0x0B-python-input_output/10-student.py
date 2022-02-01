#!/usr/bin/python3
'''comment'''


class Student:
    '''comments'''

    def __init__(self, first_name, last_name, age):
        '''comments'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''comment'''
        res = {}
        if type(attrs) is list:
            for key in attrs:
                if key in self.__dict__:
                    res[key] = self.__dict__[key]
            return res
        else:
            return self.__dict__
