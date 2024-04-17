"""
Make a list of your own. Make two more empty list like odd and even. Put all the even numbers from original list to even and odd numbers to 
odd and print both lists. (Don't remove anything from original one).
"""
from typing import List


def oddEvenList(lst: List[int]) -> None:
    odd = []
    even = []
    """
    Method 1
    for i in range(0, len(lst)):
        if lst[i] % 2 == 0:
            even.append(lst[i])
        else:
            odd.append(lst[i])
    """
    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print(f"Even list = {even}")
    print(f"Odd list = {odd}")


my_list = [56, 31, 9014, 5499, 112, 100]
oddEvenList(my_list)
