for i in range(1, 6):
    for j in range(1, 5 - i + 1):
        print(" ", end=" ")
    for k in range(i, 0, -1):
        print(k, end=" ")
    print()
