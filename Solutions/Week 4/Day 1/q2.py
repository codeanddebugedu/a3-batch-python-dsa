"""
Write a function to remove duplicates from a list and print them.
"""

from typing import List


def removeDuplicates(lst: List[int]) -> None:
    result = []
    """
    Method 1
    for i in range(0, len(lst)):
        if lst[i] not in result:
            result.append(lst[i])
    """
    for i in lst:
        if i not in result:
            result.append(i)
    print(result)


my_list = [34, 96, 34, 34, 51, 27, 96, 96, 11, 34]
removeDuplicates(my_list)
