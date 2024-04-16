"""
Write a python program which prints all the 
values whose count is greater than 3. 
(Make sure to make a list with at least 15 numbers)
"""
from typing import List


def printGreaterThanThree(lst: List[int]) -> None:
    result = []
    for i in lst:
        if lst.count(i) > 3:
            if i not in result:
                result.append(i)
    print(result)


my_list: List[int] = [34, 96, 34, 65, 51, 27, 96, 96, 11, 34, 34, 34, 51, 51, 51]

printGreaterThanThree(my_list)
