char = "Hhj438&*&$*#(     AHWUuda121&*(^$#*&))"

"""
Capital letters = 5
Small letters = 5
Digits = 6
Spaces = 5
Symbols = 17
"""
cap_letter, small_letter, digits, spaces, symbols = 0, 0, 0, 0, 0
for ch in char:
    ascii_code = ord(ch)
    if ascii_code >= 65 and ascii_code <= 90:
        cap_letter += 1
    elif ascii_code >= 97 and ascii_code <= 122:
        small_letter += 1
    elif ascii_code >= 48 and ascii_code <= 57:
        digits += 1
    elif ascii_code == 32:
        spaces += 1
    else:
        symbols += 1
print(cap_letter, small_letter, digits, spaces, symbols)
