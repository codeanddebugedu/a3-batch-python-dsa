from typing import List


def listSlice(lst: List, start: int, end: int):
    print(lst[end : start - 1 : -1])


my_list = [10, -5, 8, 3, -1, -9, 7, 2]
listSlice(my_list, 2, 5)
