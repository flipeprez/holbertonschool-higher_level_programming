#!/usr/bin/python3
import unittest
import os
from models.rectangle import Rectangle
import json
from io import StringIO
import sys

'''test for Rectangle '''


class test_rectangle(unittest.TestCase):
    '''Test rectangle'''

    def setUp(self):
        '''Initializing instance with width and height'''
        self.r = Rectangle(5, 10)

    def tearDown(self):
        '''Deleting instance'''
        del self.r

    def test_width(self):
        '''Test Rectangle getter'''
        self.assertEqual(5, self.r.width)

    def test_height(self):
        '''Testing Rectangle getter'''
        self.assertEqual(10, self.r.height)

    def test_x(self):
        '''Testing Rectangle x getter and setter'''

        self.r.x = 54
        self.assertEqual(54, self.r.x)
        self.assertEqual(0, self.r.y)

    def test_y(self):
        '''Testing Rectangle y getter and setter'''

        self.r.y = 45
        self.assertEqual(45, self.r.y)
        self.assertEqual(0, self.r.x)

    def test_rectangle_id(self):
        '''Test the id Rectangle'''
        rect = Rectangle(1, 3, 0, 0, 199)
        self.assertEqual(199, rect.id)

    def test_width_string(self):
        '''Test different type than int'''
        with self.assertRaises(TypeError):
            rect = Rectangle("1", 5)

    def test_width_bool(self):
        '''Test different type than int'''
        with self.assertRaises(TypeError):
            rect = Rectangle(True, 5)

    def test_width_list(self):
        '''Test different type than int'''
        with self.assertRaises(TypeError):
            rect = Rectangle([10, 6], 5)

    def test_height_string(self):
        '''Test different type  than int'''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, "5")
