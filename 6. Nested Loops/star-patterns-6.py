n = 7

for i in range(1, n // 2 + 2):
    for j in range(1, n // 2 - i + 2):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print(k, end=" ")
    print()

for i in range(n // 2, 0, -1):
    for j in range(1, n // 2 - i + 2):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print(k, end=" ")
    print()
