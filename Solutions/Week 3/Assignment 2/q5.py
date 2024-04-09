"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""


def pattern(n: int) -> None:
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


pattern(5)
