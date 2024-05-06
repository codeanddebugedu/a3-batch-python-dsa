def count_letters_ascii(input_string: str) -> int:
    count = 0
    for char in input_string:
        if ord("a") <= ord(char.lower()) <= ord("z"):
            count += 1
    return count


print(count_letters_ascii("Ani1rud666"))
