"""
Ask a string from user. Print how many spaces are there in that string.
"""


def countSpaces(string: str) -> int:
    count = 0
    for ch in string:
        # if ch == " ":
        #     count += 1
        if ord(ch) == 32:
            count += 1

    return count


print(countSpaces("an jdw hdkjwa"))
