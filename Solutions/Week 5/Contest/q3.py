"""
1st way
"""


def convertToUppercase(s: str) -> str:
    upper_count = sum(1 for c in s[:4] if c.isupper())
    if upper_count >= 2:
        return s.upper()
    return s


result = convertToUppercase("HelLo")
print(result)

result = convertToUppercase("Helo")
print(result)
