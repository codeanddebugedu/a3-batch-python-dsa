"""
Given a string S, containing numeric words, the task is to 
convert the given string to the actual number.
"""

help_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}

string = "zero four zero one"


res = "".join(help_dict[ele] for ele in string.split())

print(res)
