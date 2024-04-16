"""
Write a Python Program to find sum and average of List in Python.
"""

from typing import List


def sumAverage(lst: List[int | float]) -> None:
    total = 0
    for i in lst:
        total = total + i
    print(f"Total = {total}")

    average = total / len(lst)
    print(f"Average = {average}")


my_list: List[int | float] = [34, 96, 34, 65.34, 51, 27, 96.12, 96, 11, 34]
sumAverage(my_list)
