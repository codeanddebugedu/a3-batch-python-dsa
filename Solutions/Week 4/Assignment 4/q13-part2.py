def countCharacters(string: str):
    capital_count = 0
    small_count = 0
    space_count = 0
    digit_count = 0
    symbol_count = 0

    for char in string:
        if 65 <= ord(char) <= 90:
            capital_count += 1
        elif 97 <= ord(char) <= 122:
            small_count += 1
        elif ord(char) == 32:
            space_count += 1
        elif 48 <= ord(char) <= 57:
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
