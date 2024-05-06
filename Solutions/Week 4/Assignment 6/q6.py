"""
Write a function which accepts a String and another string 
(which will be a single character) as a parameter. Join that string along with that character.
"""


def joinString(string: str, char: str) -> str:
    words = string.split()
    result = char.join(i for i in words)
    return result

    # Single line
    # return char.join(i for i in string.split())


r = joinString("hello world", "%")
print(r)
