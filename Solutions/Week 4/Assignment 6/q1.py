"""
Ask a string from user. If the length of string is odd, 
then change all the capital letters to small and vice versa, 
but if the length of string is even, reverse the string. 
Do this using a function and return the output
"""


def changeString(string: str) -> str:
    if len(string) % 2 == 0:
        return string[::-1]
    return string.swapcase()


r = changeString("a432432eradADAWplaAne")
print(r)
r = changeString("a432432eradADAWplaAn")
print(r)
