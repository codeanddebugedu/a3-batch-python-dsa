# Method 1
def max_ascii_character(input_string):
    max_char = max(input_string, key=lambda x: ord(x))
    return max_char


# Method 2
def max_ascii_character2(input_string):
    max_char = ""
    max_ascii = 0
    for char in input_string:
        char_ascii = ord(char)
        if char_ascii > max_ascii:
            max_char = char
            max_ascii = char_ascii
    return max_char
