"""
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""


def pattern(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(n, i - 1, -1):
            print(j, end=" ")
        print()


pattern(5)
