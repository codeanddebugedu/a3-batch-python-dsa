"""
Ask a string from user. Print how many characters are there which are not alphabets
"""


def countNotAlphabets(string: str) -> int:
    # Method 1
    """
    count = 0
    for ch in string:
        if not ch.isalpha():
            count += 1
    return count
    """

    new_string = string.lower()
    count = 0

    for ch in new_string:
        ascii_code = ord(ch)
        if not (ascii_code >= 97 and ascii_code <= 122):
            count += 1

    return count


print(countNotAlphabets("a bv ^&*"))
