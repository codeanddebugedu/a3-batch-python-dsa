"""
Ask a string from user. Print how the count of alphabets (a-z or A-Z) in that string.
"""


def countAlphabets(string: str) -> int:
    # Method 1
    """
    count = 0
    new_string = string.lower()
    for ch in new_string:
        ascii_code = ord(ch)
        if ascii_code >= 97 and ascii_code <= 122:
            count += 1
    return count
    """

    count = 0
    for ch in string:
        if ch.isalpha():
            count += 1
    return count
