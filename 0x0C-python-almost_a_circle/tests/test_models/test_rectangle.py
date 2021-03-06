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

    def test_height_bool(self):
        '''test different type than int'''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, True)

    def test_height_list(self):
        '''testdifferent type than int'''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, [7, 8])

    def test_x_string(self):
        '''test different type than int'''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, "33")

    def test_x_bool(self):
        '''test different type than int'''
        with self.assertRaises(TypeError):
            rect = Rectangle(2, 3, True)

    def test_x_list(self):
        '''test different types than int'''
        with self.assertRaises(TypeError):
            rect = Rectangle(3, 4, [8, 9])

    def test_y_str(self):
        '''test different types than int'''
        with self.assertRaises(TypeError):
            rect = Rectangle(4, 2, 3, "33")

    def test_y_bool(self):
        '''test different types than int'''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, 3, True)

    def test_y_list(self):
        '''test different types than int'''
        with self.assertRaises(TypeError):
            rect = Rectangle(2, 3, 4, [7, 8])

    def test_width_negative(self):
        '''test width with negatives'''
        with self.assertRaises(ValueError):
            rect = Rectangle(9, -1)

    def test_height_negative(self):
        '''test height with negatives'''
        with self.assertRaises(ValueError):
            rect = Rectangle(-3, 5)

    def test_x_negative(self):
        '''test x with negatives'''
        with self.assertRaises(ValueError):
            rect = Rectangle(2, 4, -5)

    def test_y_negative(self):
        '''test y with negative'''
        with self.assertRaises(ValueError):
            rect = Rectangle(3, 5, 7, -3)

    def test_width_zero(self):
        '''test width with zero'''
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 8)

    def test_height_zero(self):
        '''test height with zero'''
        with self.assertRaises(ValueError):
            rect = Rectangle(7, 0)

    def test_width_float(self):
        '''test width with float'''
        with self.assertRaises(TypeError):
            rect = Rectangle(1.02, 6)

    def test_height_float(self):
        '''test height with zero'''
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 7.09)

    def test_x_float(self):
        '''test x xith float'''
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 6, 7.89)

    def test_y_float(self):
        '''test y with float'''
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 6, 7, 8.99)

    def test_area(self):
        '''test area'''
        self.assertEqual(self.r.area(), 5 * 10)
        rect = Rectangle(3, 9, 8, 8, 2)
        self.assertEqual(rect.area(), 3 * 9)

    def test_str_for_rec(self):
        '''test str for rec'''
        r = Rectangle(5, 9, 7, 4, 88)
        self.assertEqual(r.__str__(), "[Rectangle] (88) 7/4 - 5/9")

    def test_update(self):
        '''test update method'''
        self.r.update(23)
        self.assertEqual(23, self.r.id)

    def test_update_width(self):
        '''test update width'''
        self.r.update(23, 45)
        self.assertEqual(45, self.r.width)

    def test_update_height(self):
        '''test update height'''
        self.r.update(23, 45, 24)
        self.assertEqual(24, self.r.height)

    def test_update_x(self):
        self.r.update(23, 45, 24, 6)
        self.assertEqual(6, self.r.x)

    def test_update_y(self):
        self.r.update(23, 45, 24, 6, 9)
        self.assertEqual(9, self.r.y)

