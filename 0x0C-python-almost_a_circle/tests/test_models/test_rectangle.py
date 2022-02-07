#!/usr/bin/python3
'''module test'''
import unnitest
from models.rectangle import Rectangle


class testinit(unitest, TestCase)
def testinit(self):
    '''tesrt init'''
    a = rectangle()
    self.assertEqual(a.id, 1)
    b = rectangle()
    self.assertEqual(b.id, 2)
    c = rectangle(33)
    self.assertEqual(c.id, 33)
    d = rectangle(-14)
    self.assertEqual(d.id, -14)
