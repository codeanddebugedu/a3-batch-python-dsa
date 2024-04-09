"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""


def pattern(n: int) -> None:
    for _ in range(1, n + 1):
        for j in range(1, 6):
            print(j, end=" ")
        print()


pattern(10)
