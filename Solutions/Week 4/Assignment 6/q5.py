"""
Write a function which accepts a String as a parameter and return each word being in reverse.
"""


def reverseWords(string: str) -> str:
    words = string.split()
    result = " ".join(i[::-1] for i in words)
    return result

    # Shortcut
    # return " ".join(i[::-1] for i in string.split())


r = reverseWords("python is great")
print(r)
