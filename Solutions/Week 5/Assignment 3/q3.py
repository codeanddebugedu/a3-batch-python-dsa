"""
Write a Python program to print a dictionary line by line.
Sample Output
Dict = {  "Sam" : {"M1" : 89, "M2" : 56, "M3" : 89},
               "Suresh" : {"M1" : 49, "M2" : 96, "M3" : 89} }

Sam
M1 : 89
M2 : 56
M3 : 89
Suresh
M1 : 49
M2 : 96
M3 : 89
"""

from typing import Dict


def printDictionary(dictionary: Dict) -> None:
    for key, value in dictionary.items():
        print(key)
        for k, v in value.items():
            print(f"{k} : {v}")


printDictionary(
    {
        "Sam": {"M1": 89, "M2": 56, "M3": 89},
        "Suresh": {"M1": 49, "M2": 96, "M3": 89},
    }
)
