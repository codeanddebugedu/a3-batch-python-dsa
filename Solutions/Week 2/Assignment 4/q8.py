"""
Write a function named pattern which accepts an integer
n as an argument. Then print the following pattern.

1 4 9 16...
"""


def pattern(n):
    i = 1
    while i <= n:
        print(i**2, end=" ")
        i += 1
    print()


pattern(10)
