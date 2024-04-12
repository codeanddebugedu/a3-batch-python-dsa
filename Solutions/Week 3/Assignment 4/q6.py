"""
Create a function sumCountOddEven that accepts an 
List of Integers and print how many sum of even and odd numbers are there.

"""
from typing import List


def sumCountOddEven(lst: List[int]):
    even_sum: int = 0
    odd_sum: int = 0
    for i in range(0, len(lst)):
        if lst[i] % 2 == 0:
            even_sum = even_sum + lst[i]
        else:
            odd_sum = odd_sum + lst[i]
    print(f"Even numbers sum = {even_sum}")
    print(f"Odd numbers sum = {odd_sum}")


my_list = [34, 11, 91, 59, 33, 22]
sumCountOddEven(my_list)
