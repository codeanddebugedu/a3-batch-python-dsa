from typing import List


def interchange(lst: List):
    # lst[0], lst[-1] = lst[-1] = lst[0]  # Method 1

    # Method 2
    temp = lst[0]
    lst[0] = lst[-1]
    lst[-1] = temp


my_list = ["Anirudh", 6, 4, 110.654, True, -54]
interchange(my_list)
print(my_list)
