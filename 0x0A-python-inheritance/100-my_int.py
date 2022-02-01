#!/usr/bin/python3
'''def class'''

class Myint(int):
    '''coment'''
    def __init__(self, number):
        '''comment'''
        self.number = number
    def __ne__(self, val):
        '''comment'''
        return (self.number == val)
    def __eq__(self, val):
        '''comment'''
        return (self.number != val)
    def __str__(self):
        '''comment'''
        return (str(self.number))
