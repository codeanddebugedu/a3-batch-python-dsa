"""
Write a function which accepts a String as a parameter and return the reversed words as a String.
"""


def reverseWords(string: str) -> str:
    words = string.split()
    words.reverse()
    result = " ".join(i for i in words)
    return result

    # Shortcut
    # return " ".join(i for i in reversed(string.split()))


print(reverseWords("python is great"))
