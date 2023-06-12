#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lent_a = len(tuple_a)
    lent_b = len(tuple_b)
    if lent_a < 2:
        tuple_a += 0, 0
    if lent_b < 2:
        tuple_b += 0, 0

    add_tup = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (add_tup)
