"""
Python program to find the size of a Dictionary. 
Basically print how many total key-value pair are there.
"""

from typing import Dict


def countKeys(dictionary: Dict) -> int:
    return len(dictionary.keys())


print(countKeys({}))
print(countKeys({"name": "xyz"}))
