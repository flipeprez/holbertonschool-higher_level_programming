#!/usr/bin/python3
''' define class '''


class MyList(list):
    '''public instance method'''
    def print_sorted(self):
        print(sorted(self))
