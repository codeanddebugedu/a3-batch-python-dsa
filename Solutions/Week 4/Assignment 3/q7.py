"""
Create a function findLargest that accepts an 
List of Integers and returns the largest number from the list.
"""
from typing import List


def findLargest(lst: List[int]) -> int:
    largest = lst[0]
    for i in range(0, len(lst)):
        if lst[i] > largest:
            largest = lst[i]
    return largest


my_list = [34, 11, 91, 59, 33, 22]
x = findLargest(my_list)

print(x)
