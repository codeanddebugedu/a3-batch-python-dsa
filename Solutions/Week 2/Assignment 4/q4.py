"""
Create a function named pattern which takes an integer as an
input and print the following pattern.

10 20 30 40 50
"""


def pattern(n):
    i = 1
    num = 10
    while i <= n:
        print(num, end=" ")
        num = num + 10
        i = i + 1
    print()


pattern(5)
