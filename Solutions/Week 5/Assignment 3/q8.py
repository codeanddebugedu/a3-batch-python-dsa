"""
Create a Python function to reverse a dictionary (swap keys and values). 
Make sure the values are dierent.
Original dictionary: {'a': 1, 'b': 2, 'c': 3}
Reversed dictionary:
{1: 'a', 2: 'b', 3: 'c'
"""

from typing import Dict


def swapDictionary(dictionary: Dict) -> Dict:
    reversed_dict = {}
    for k, v in dictionary.items():
        reversed_dict[v] = k
    return reversed_dict


my_dict = {"a": 1, "b": 2, "c": 3}
result = swapDictionary(my_dict)
print(my_dict)
print(result)
