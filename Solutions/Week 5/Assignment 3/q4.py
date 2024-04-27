"""
Write a Python program to Convert two lists into a dictionary
Sample Output
keys = ["One", "Two", "Three", "Four", "Five"]
values = [1, 2, 3, 4, 5]
Convert Two List to Dict = {'One' : 1, 'Two' : 2, 'Three' : 3, 'Four' : 4, 'Five' : 5
"""

from typing import Dict, List


def convertToDictionary(lst1: List, lst2: List) -> Dict:
    dictionary = {}
    for i in range(len(lst1)):
        # dictionary.update({lst1[i]: lst2[i]})
        dictionary[lst1[i]] = lst2[i]
    return dictionary


keys = ["One", "Two", "Three", "Four", "Five"]
values = [1, 2, 3, 4, 5]
my_dict = convertToDictionary(keys, values)
print(my_dict)
