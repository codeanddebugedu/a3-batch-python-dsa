"""
Create a Python program to find the dierence between two dictionaries.
First dictionary: {'a': 1, 'b': 2, 'c': 3}
Second dictionary: {'b': 2, 'c': 4, 'd': 5}

OUTPUT:
Keys present only in the first dictionary: ['a']
Keys present only in the second dictionary: ['d']
Keys present in both dictionaries: ['b', 'c']
"""


def findDifference(dictionary1, dictionary2) -> None:
    present_in_dict1 = []
    present_in_both = []
    for k in dictionary1:
        if k not in dictionary2:
            present_in_dict1.append(k)
        else:
            present_in_both.append(k)

    present_in_dict2 = []
    for k in dictionary2:
        if k not in dictionary1:
            present_in_dict2.append(k)

    print(f"Keys present only in the first dictionary: {present_in_dict1}")
    print(f"Keys present only in the second dictionary: {present_in_dict2}")
    print(f"Keys present in both dictionaries: {present_in_both}")


findDifference({"a": 1, "b": 2, "c": 3}, {"b": 2, "c": 4, "d": 5})
