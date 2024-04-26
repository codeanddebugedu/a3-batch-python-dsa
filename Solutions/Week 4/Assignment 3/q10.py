"""
Create a function updateOddEven that accepts an List of Integers 
and update all the even numbers to increment by 1 and update 
all the odd numbers to decrement by 1.
"""
from typing import List


def updateOddEven(lst: List[int]) -> None:
    for i in range(0, len(lst)):
        if lst[i] % 2 == 0:
            lst[i] = lst[i] + 1
        else:
            lst[i] = lst[i] - 1


my_list = [34, 11, 91, 59, 33, 22]
updateOddEven(my_list)

print(my_list)
