"""
Write a python program to ask a string from user. 
Then count the number of vowels and number of consonants in that string.
"""
from typing import Tuple


def count_vowels_and_consonants(string: str) -> Tuple[int, int]:
    vowels = 0
    consonants = 0
    new_string = string.lower()  # Convert to lowercase

    for ch in new_string:
        if ch.isalpha():
            if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants


def count_vowels_and_consonants_2(string: str) -> Tuple[int, int]:
    vowels = 0
    consonants = 0
    new_string = string.lower()  # Convert to lowercase

    for ch in new_string:
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants


v, c = count_vowels_and_consonants("321AeI98bvmncxb")
print(v)
print(c)

v, c = count_vowels_and_consonants_2("321AeI98bvmncxb")
print(v)
print(c)
