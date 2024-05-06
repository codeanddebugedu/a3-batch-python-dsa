# Method 1
def toggle_case_ascii(input_string: str) -> str:
    toggled_chars = [
        char.upper() if char.islower() else char.lower() for char in input_string
    ]
    return "".join(toggled_chars)


# Method 2
def toggle_case_ascii2(input_string: str) -> str:
    result = ""
    for char in input_string:
        if "a" <= char <= "z":
            result += chr(ord(char) - 32)
        elif "A" <= char <= "Z":
            result += chr(ord(char) + 32)
        else:
            result += char
    return result
