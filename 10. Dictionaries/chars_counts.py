from typing import Dict


def countChars(string: str) -> Dict[str, int]:
    n = len(string)
    freq_map = {}
    for i in range(n):
        freq_map[string[i]] = freq_map.get(string[i], 0) + 1
    return freq_map


a = "python is a great language"

print(countChars(a))
