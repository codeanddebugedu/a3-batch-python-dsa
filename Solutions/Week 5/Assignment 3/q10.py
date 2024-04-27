"""
Write a Python program to sort a dictionary by its keys in ascending order.
Original dictionary: {'b': 2, 'a': 1, 'c': 3}
Sorted dictionary by keys:
{'a': 1, 'b': 2, 'c': 3}
"""

from typing import Dict


def sortByKeys(dictionary: Dict) -> Dict:
    return dict(sorted(dictionary.items(), key=lambda x: x[0]))


my_dict = {"b": 2, "a": 1, "c": 3}

result = sortByKeys(my_dict)

print(my_dict)
print(result)
