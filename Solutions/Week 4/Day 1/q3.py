"""
Write a Python function that takes two lists and returns True
if they have at least one common element.
"""
from typing import List


def isCommon(lst1: List, lst2: List) -> bool:
    for i in lst1:
        if i in lst2:
            return True
    return False


my_list1 = ["Anirudh", "xyz", 98, 11.908, 93, -100]
my_list2 = [9008, 9102, 4311, 222]

print(isCommon(my_list1, my_list2))
