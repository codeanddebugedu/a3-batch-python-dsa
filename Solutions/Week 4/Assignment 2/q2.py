from typing import List


def listSlice(lst: List, start: int, end: int):
    print(lst[start : end + 1])


my_list = ["Anirudh", 6, 4, 110.654, True, -54]
listSlice(my_list, 2, 4)
