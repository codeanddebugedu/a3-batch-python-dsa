"""
Write a Python program to find the maximum and minimum value in a dictionary.
"""

from typing import Dict


def maximum(dictionary: Dict) -> int | float:
    max_num = float("-inf")  # Most negative number
    for v in dictionary.values():
        if v > max_num:
            max_num = v
    return max_num


def minimum(dictionary: Dict) -> int | float:
    min_num = float("inf")  # Most positive number
    for v in dictionary.values():
        if v < min_num:
            min_num = v
    return min_num


my_dict = {"Anirudh": 54.6, "Akul": 12, "Nihar": 35.123, "Sanjay": 111}

mini = minimum(my_dict)
maxi = maximum(my_dict)

print(f"Minimum = {mini}")
print(f"Maximum = {maxi}")
