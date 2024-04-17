"""
Write a program to remove the nth index element from a list using a function.
"""
from typing import List


def removeNth(lst: List, n: int) -> None:
    lst.pop(n)


my_list = [9008, 9102, 4311, 222, 98]
removeNth(my_list, 2)
print(my_list)
