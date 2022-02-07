#!/usr/bin/python3
'''module test'''
import unnitest
from models.base import Base 


class testinit(unitest, TestCase):
def testinit(self):
    '''tesrt init'''
    a = base()
    self.assertEqual(a.id, 1)
    b = base()
    self.assertEqual(b.id, 2)
    c = base(33)
    self.assertEqual(c.id, 33)
    d = base(-14)
    self.assertEqual(d.id, -14)
