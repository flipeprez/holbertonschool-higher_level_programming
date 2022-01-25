#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_none_value(self):
        '''test'''
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_empty_list(self):
        '''test'''
        self.assertIsNone(max_integer([]))

    def test_no_param(self):
        '''test'''
        self.assertIsNone(max_integer())

    def test_no_ints(self):
        '''test'''
        with self.assertRaises(TypeError):
            max_integer([1, "hello", 2, 3])
