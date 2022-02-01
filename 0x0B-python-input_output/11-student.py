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

    def reload_from_json(self, json):
        '''comment'''
        sarasa = dict(json)
        for key in dict(self.__dict__):
            if key in json:
                self.__dict__[key] = sarasa[key]
