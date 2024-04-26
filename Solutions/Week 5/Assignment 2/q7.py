"""
Write a Python function that takes a dictionary as input where the 
values are lists of integers. 
The function should return a new dictionary where the values 
are lists containing only the even integers from the original lists
"""

from typing import Dict


def filterEvenIntegers(dictionary: Dict) -> Dict:
    # Method 1
    """
    for k, v in dictionary.items():
        even_list = []
        for i in v:
            if i % 2 == 0:
                even_list.append(i)
        dictionary[k] = even_list
    return dictionary
    """
    filtered_dict = {}
    for key, value in dictionary.items():  # Optimal Way
        filtered_dict[key] = [num for num in value if num % 2 == 0]
    return filtered_dict


input_dict = {"a": [1, 2, 3, 4, 5], "b": [10, 11, 12, 13, 14]}
filtered_dict = filterEvenIntegers(input_dict)
print(filtered_dict)
