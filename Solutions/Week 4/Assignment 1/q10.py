"""
Ask 10 numbers from the user and put them into the list. 
Now remove all the even numbers from that list.
"""

from typing import List


def removeEven(lst: List[int]) -> None:
    result = []
    for i in lst:
        if i % 2 == 1:
            result.append(i)
    print(result)


my_list = []
for _ in range(10):
    num: int = int(input("Enter a number = "))
    my_list.append(num)

removeEven(my_list)
