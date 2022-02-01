#!/usr/bin/python3
'''comment'''


class Student:
    '''comments'''

    def __init__(self, first_name, last_name, age):
        '''comments'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''comment'''
        return self.__dict__
