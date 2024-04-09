def pattern(n: int) -> None:
    for i in range(1, n // 2 + 2):
        for j in range(n // 2 - i + 1):
            print(" ", end=" ")
        for k in range(2 * i - 1):
            print(i, end=" ")
        print()
    for i in range(n // 2, -1, -1):
        for j in range(n // 2 - i + 1):
            print(" ", end=" ")
        for k in range(2 * i - 1):
            print(i, end=" ")
        print()


pattern(13)
