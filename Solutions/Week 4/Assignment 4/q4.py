"""
Write a Python program to reverse a tuple.
"""
from typing import Tuple


def reverseTuple(tup: Tuple) -> Tuple:
    # MEthod 1
    # lst = list(tup)
    # lst.reverse()
    # new_tup = tuple(lst)
    # return new_tup

    return tuple(reversed(tup))


my_tuple = (1, 2, "Anirudh", False, "OK")

r = reverseTuple(my_tuple)
print(r)
