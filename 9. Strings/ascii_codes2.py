char = "Hhj438&*&$*#(     AHWUuda121&*(^$#*&))"

cap_letter, small_letter, digits, spaces, symbols = 0, 0, 0, 0, 0
for ch in char:
    ascii_code = ord(ch)
    if "A" <= ch <= "Z":
        cap_letter += 1
    elif "a" <= ch <= "z":
        small_letter += 1
    elif "0" <= ch <= "9":
        digits += 1
    elif ascii_code == 32:
        spaces += 1
    else:
        symbols += 1
print(cap_letter, small_letter, digits, spaces, symbols)
