def count_digits_ascii(input_string: str) -> int:
    count = 0
    for char in input_string:
        if ord("0") <= ord(char) <= ord("9"):
            count += 1
    return count


print(count_digits_ascii("Room 1001"))
