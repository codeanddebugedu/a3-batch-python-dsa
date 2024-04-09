def pattern(n: int) -> None:
    for i in range(1, n // 2 + 2):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    for k in range(n // 2, -1, -1):
        for l in range(1, k + 1):
            print(l, end=" ")
        print()


pattern(13)
