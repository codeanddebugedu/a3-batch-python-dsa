def has_special_characters_ascii(input_string: str) -> bool:
    for char in input_string:
        if not (
            ord("a") <= ord(char.lower()) <= ord("z")
            or ord("0") <= ord(char) <= ord("9")
        ):
            return True
    return False
