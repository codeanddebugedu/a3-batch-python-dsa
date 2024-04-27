"""
Given a list of strings, concatenate them into a single string separated by spaces.
For example, given the input ["Hello", "World", "Python"], 
the output should be "Hello World Python".

Make a list on your own.Don't use the JOIN function
"""

from typing import List


def joinWords(words: List[str]) -> str:
    result = ""
    for word in words:
        result += word
        result += " "
    return result


my_words = ["Hello", "World", "Python"]

s = joinWords(my_words)
print(s)
