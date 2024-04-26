"""
Create a function countOddEven that accepts an List of Integers 
and print how many even and odd numbers are there
"""
from typing import List


def countOddEven(lst: List[int]):
    even_count: int = 0
    odd_count: int = 0
    for i in range(0, len(lst)):
        if lst[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(f"Total even numbers = {even_count}")
    print(f"Total odd numbers = {odd_count}")


my_list = [34, 11, 91, 59, 33, 22]
countOddEven(my_list)
