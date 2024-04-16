from typing import List


def additionElement(lst: List[int]):
    if len(lst) == 1:
        print("Cannot add 2nd and last 2nd element as not enough elements in list")
        return
    print(lst[1] + lst[-2])


my_list = [43, 11, 92, 22]
additionElement(my_list)
