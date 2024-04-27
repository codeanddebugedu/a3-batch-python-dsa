def convertToUppercase(s: str):
    upper_count = 0
    for c in s[:4]:
        if c.isupper():
            upper_count += 1
    if upper_count >= 2:
        return s.upper()
    return s


result = convertToUppercase("HelLo")
print(result)

result = convertToUppercase("Helo")
print(result)
