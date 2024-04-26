from typing import List


def listSlice(lst: List, start: int, end: int):
    result: List = []
    for i in range(start, end + 1):
        result.append(lst[i])
    print(result)


my_list = ["Anirudh", 6, 4, 110.654, True, -54]
listSlice(my_list, 2, 4)
