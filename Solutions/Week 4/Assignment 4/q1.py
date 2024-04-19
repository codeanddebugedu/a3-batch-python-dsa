"""
Write a Python program to get the 4th element from the last element of a tuple.
"""

from typing import Tuple


def fourthElementFromLast(tup: Tuple) -> None:
    if len(tup) < 4:
        print("Not enough elements")
        return

    print(tup[-4])


fourthElementFromLast((1, 2, 3))
fourthElementFromLast((54, 14, 71, 85, 44))
