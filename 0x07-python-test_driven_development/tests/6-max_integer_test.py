#!/usr/bin/python3
"""comment"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_none_value(self):
        '''comment'''
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_right_output(self):
        '''comment'''
        self.assertEqual(max_integer([1, 6, 100, 4, 0, -1, 10]), 100)

    def test_empty_list(self):
        '''comment'''
        self.assertIsNone(max_integer([]))

    def test_no_param(self):
        '''comment'''
        self.assertIsNone(max_integer())

    def test_equal_values(self): 
        '''comment'''
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_no_ints(self): 
        '''comment'''
        with self.assertRaises(TypeError):
            max_integer([1, "hello", 2, 3])

    def test_only_negatives(self): 
        '''comment'''
        self.assertEqual(max_integer([-10, -100, -6, -3, -1]), -1)

    def test_begining(self):
        '''comment'''
        self.assertEqual(max_integer([100, 1, 1, 1]), 100)

    def test_one(self):
        '''comment'''
        self.assertEqual(max_integer([1]), 1)
