# Method 1
def sum_ascii_values(input_string: str) -> int:
    return sum(ord(char) for char in input_string)


def sum_ascii_values2(input_string: str) -> int:
    count = 0
    for char in input_string:
        count += ord(char)
    return count
