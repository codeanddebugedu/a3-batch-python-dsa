"""
Write a Python program to combine two dictionary by adding values
for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}
"""


def combineDictionary(d1, d2):
    combined_dict = {}

    for key in d1:
        combined_dict[key] = d1[key] + d2.get(key, 0)

    # Do for keys from d2 not present in d1
    for key in d2:
        if key not in d1:
            combined_dict[key] = d2[key]

    return combined_dict


# OPTIMAL WAY
def combineDictionary1(d1, d2):
    combined_dict = {}

    # This combines keys of both d1 and d2
    for key in d1.keys() | d2.keys():
        combined_dict[key] = d1.get(key, 0) + d2.get(key, 0)

    return combined_dict


d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}

result = combineDictionary(d1, d2)
print(result)

result1 = combineDictionary1(d1, d2)
print(result1)
