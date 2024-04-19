"""
Create a function calculatePrime that accepts an List of Integers 
and print all the prime numbers in that list.

METHOD 1 (Nested Loops)
"""
from typing import List


def calculatePrime(lst: List[int]) -> None:
    for i in range(0, len(lst)):
        factors = 0
        num = lst[i]
        for j in range(1, num + 1):
            if num % j == 0:
                factors += 1
        if factors == 2:
            print(num, end=" ")


my_list = [34, 11, 91, 59, 33, 22]
calculatePrime(my_list)
