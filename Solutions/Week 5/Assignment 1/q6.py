"""
Write a Python program to check if a dictionary is empty or not.
"""

from typing import Dict


def isEmpty(dictionary: Dict) -> bool:
    # Method 1 (Best way)
    """
    if not dictionary:
        return True
    return False
    """

    # Method 2
    """
    if len(dictionary.keys()) == 0:
        return True
    return False
    """

    # Method 3
    count = 0
    for i in dictionary.keys():
        count += 1
    if count == 0:
        return True
    return False


print(isEmpty({}))
print(isEmpty({"name": "xyz"}))
