# Method 1
def replace_non_alphabetic_ascii(input_string: str) -> str:
    replaced_chars = [char if char.isalpha() else " " for char in input_string]
    return "".join(replaced_chars)


# Method 2
def replace_non_alphabetic_ascii2(input_string: str) -> str:
    result = ""
    for char in input_string:
        if char.isalpha():
            result += char
        else:
            result += " "
    return result
