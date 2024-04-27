"""
Create a function named arrangeChars which takes a string as a parameter. 
Now return a string with max frequency chars at start.
"""


def arrangeChars(string: str) -> str:
    characters_count = {}
    for ch in string:
        characters_count[ch] = characters_count.get(ch, 0) + 1
    characters_count = dict(
        sorted(characters_count.items(), key=lambda x: x[1], reverse=True)
    )
    result = ""
    for char, count in characters_count.items():
        result += char * count
    return result


print(arrangeChars("aaeroplane"))
