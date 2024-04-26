a = "HelLo WOOrLLLDd"

# Via Values
count = 0
for ch in a:
    if ch == "o" or ch == "O":
        count += 1

print(count)

# Via Index
count = 0
for index in range(0, len(a)):
    if a[index] == "O" or a[index] == "o":
        count += 1

print(count)
