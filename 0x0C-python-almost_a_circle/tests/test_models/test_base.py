#!/usr/bin/python3
'''module test'''
import unittest
from models.base import Base
from models.square import Square
import json


class TestForFase(unittest.TestCase):
    '''testing for base class'''

    def test_id_none(self):
        '''test no id'''
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
    
    def test_id(self):
        '''giving a id'''
        b = Base(33)
        self.assertEqual(33, b.id)

    def test_id_0(self):
        '''givin 0 like id'''
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_negative(self):
        '''giving a negative'''
        b = Base(-14)
        self.assertEqual(-14, b.id,)

    def test_for_string_id(self):
        '''givining not int to id'''
        b = Base("not_a_number_id")
        self.assertEqual("not_a_number_id", b.id)

    def test_giving_list(self):
        '''giving a list for id'''
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])

    def giving_dict_id(self):
        '''giving a dict for id'''
        b = Base({'id': 321})
        self.assertEqual({'id': 321})

    def test_json_type(self):
        '''test json string'''
        S = Square(1)
        jdic = S.to_dictionary()
        jstr = Base.to_json_string([jdic])
        self.assertEqual(type(jstr), str)

    def test_json_None(self):
        '''test json str'''
        S = Square(1, 0, 0, 545)
        jdic = S.to_dictionary()
        jstr = Base.to_json_string(None)
        self.assertEqual(jstr, "[]")

    def tests_json_empty(self):
        '''test json str'''
        S = Square(1, 0, 0, 545)
        jdic = S.to_dictionary()
        jstr = Base.to_json_string([])
        self.assertEqual(jstr, "[]")
