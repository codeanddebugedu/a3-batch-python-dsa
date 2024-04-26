char = "djwkal479832hdkwjaBCNMZ^%*&(^*&1212)"

count = 0
for ch in char:
    ascii_code = ord(ch)
    if ascii_code >= 48 and ascii_code <= 57:
        count += 1
    # elif

print(count)
