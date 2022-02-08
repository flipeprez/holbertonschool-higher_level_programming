#!/usr/bin/python3
'''module test'''
import unnitest
from models.base import Base 


class testing_for_base(unitest, TestCase):
    '''testing for base class'''

        def test_id_none(self):
            '''test no id'''
        a = Base()
        self.assertEqual(1, a.id)
        b = Base()
        self.assertEqual(2, b.id)

        def test_id(self):
            '''giving a id'''
        b = Base(33)
        self.assertEqual(33, c.id)

        def test_id_0(self):
            '''givin 0 like id'''
        b = Base(0)
        self.accertEqual(0, b.id)

        def test_negative(self):
            '''giving a negative'''
        b = Base(-14)
        self.assertEqual(-54, b.id,)

        def test_for_string_id(self):
            '''givining not int to id'''
            b = Base("not_a_number_id")
            self.assertEqual("not_a_number_id", b.id)

        def test_giving_list(self):
            '''giving a list for id'''
            b = Base([1, 2, 3], b.id)

        def giving_dict_id(self):
            '''giving a dict for id'''
            b = base({'id': 321})
            self.accertEqual({'id': 321})

        def test_json_type(self):
            '''test json string'''
            S = Square(1)
            jdic = S.to_dictionary()
            jstr = Base.to_json_string([jdict])
            self.assertEqual(type(jstr), str)
            
