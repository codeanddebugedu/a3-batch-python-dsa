"""
Ask a string from user. Print the count of capital alphabets, 
small alphabets, spaces, digits and then symbols 
(whatever are left, count them in symbols).
"""


def countCharacters(string: str):
    capital_count = 0
    small_count = 0
    space_count = 0
    digit_count = 0
    symbol_count = 0

    for char in string:
        if char.isupper():
            capital_count += 1
        elif char.islower():
            small_count += 1
        elif char.isspace():
            space_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbol_count += 1

    print(f"Count of capital alphabets = {capital_count}")
    print(f"Count of small alphabets = {small_count}")
    print(f"Count of spaces = {space_count}")
    print(f"Count of digits = {digit_count}")
    print(f"Count of symbols = {symbol_count}")


user_input = input("Enter a string: ")

countCharacters(user_input)
