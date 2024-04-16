"""
Make two lists of same length and pass it to a function. 
Return a third list where each element is the sum of index.
"""
from typing import List


def addition(lst1: List[int], lst2: List[int]) -> List[int]:
    result = []

    # As we know the length are same, we will iterate via index
    for i in range(0, len(lst1)):
        result.append(lst1[i] + lst2[i])

    return result


my_list1 = [43, 11, 92, 22]
my_list2 = [-100, -200, 221, 100]

x = addition(my_list1, my_list2)
print(x)
