def reverseChar(string: str) -> str:
    words = string.split()
    return " ".join(i[::-1] for i in words)


x = reverseChar("python is good")
print(x)
