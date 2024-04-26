def secondHalfString(string: str) -> str:
    length = len(string)
    return string[length // 2 + 1 :]


print(secondHalfString("aeroplane"))
print(secondHalfString("delhi"))
print(secondHalfString("pavbhaji"))
