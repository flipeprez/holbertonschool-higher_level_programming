#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a, b = len(tuple_a), len(tuple_b)
    tutupish1 = (tuple_a[0] if a >= 1 else 0) + (tuple_b[0] if b >= 1 else 0)
    tutupish2 = (tuple_a[1] if a >= 2 else 0) + (tuple_b[1] if b >= 2 else 0)
    tutupish3 = (tutupish1, tutupish2)
    return tutupish3
