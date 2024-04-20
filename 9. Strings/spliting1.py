def reverseWords(string: str) -> str:
    words = string.split()
    words = words[::-1]
    return " ".join(words)
    # return " ".join(i for i in string.split()[::-1])


x = reverseWords("python is good")
print(x)
