from typing import List


def splitList(lst: List):
    mid: int = len(lst) // 2
    first_half = lst[:mid]
    second_half = lst[mid:]
    print(first_half)
    print(second_half)


my_list = ["Anirudh", 6, 4, 110.654, True, -54]
splitList(my_list)
