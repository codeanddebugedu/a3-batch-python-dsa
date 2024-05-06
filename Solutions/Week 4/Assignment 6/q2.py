"""
Write a function which accepts a String as a parameter and return the list of words.
"""

from typing import List


def words(string: str) -> List[str]:
    return string.split()


w = words("python is a great language")
print(w)
