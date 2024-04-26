"""
Create a function findSmallest that accepts an List of Integers 
and returns the smallest number from the list.
"""
from typing import List


def findSmallest(lst: List[int]) -> int:
    smallest = lst[0]
    for i in range(0, len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
    return smallest


my_list = [34, 11, 91, 59, 33, 22]
x = findSmallest(my_list)

print(x)
