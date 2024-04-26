"""
Given a dictionary with key-value pairs, remove all the keys with values 
greater than K, including mixed values.
Input : test_dict = {'Gfg' : 3, 'is' : 7, 'best' : 10, 'for' : 6, 'xyzx' : 'CS'}, K = 7 
Output : {'Gfg' : 3, 'for' : 6, 'xyzx' : 'CS'} 
Explanation : All values greater than K are removed. Mixed value is retained. 
Input : test_dict = {'Gfg' : 3, 'is' : 7, 'best' : 10, 'for' : 6, 'qqqq' : 'CS'}, K = 1 
Output : {'qqqq' : 'CS'} 
Explanation : Only Mixed value is retained.
"""

from typing import Dict


def removeKeys(dictionary: Dict, K: int):
    # Uncomment this, if you want to change in original dictionary
    dictt = dictionary.copy()

    keys_to_remove = []
    for key, value in dictt.items():
        if type(value) == int and value > K:
            keys_to_remove.append(key)

    for key in keys_to_remove:
        dictt.pop(key)

    return dictt


test_dict1 = {"Gfg": 3, "is": 7, "best": 10, "for": 6, "xyzx": "CS"}
test_dict2 = {"Gfg": 3, "is": 7, "best": 10, "for": 6, "qqqq": "CS"}
K1 = 7
K2 = 1

output1 = removeKeys(test_dict1, K1)
output2 = removeKeys(test_dict2, K2)

print(output1)
print(output2)
