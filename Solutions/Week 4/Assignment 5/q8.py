# Method 1
def remove_numeric_ascii(input_string: str) -> str:
    removed_chars = [
        char for char in input_string if not ord("0") <= ord(char) <= ord("9")
    ]
    return "".join(removed_chars)


# Method 2
def remove_numeric_ascii2(input_string: str) -> str:
    result = ""
    for char in input_string:
        if not ord("0") <= ord(char) <= ord("9"):
            result += char
    return result
