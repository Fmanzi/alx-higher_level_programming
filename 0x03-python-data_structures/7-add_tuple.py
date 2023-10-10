#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1, a2 = tuple_a[:2]
    b1, b2 = tuple_b[:2]
    
    result1 = a1 + b1
    result2 = a2 + b2
    return (result1, result2)
