"""
Create a function named pattern which takes an integer as 
an input and print the following pattern.

1 2 4 8 ...
"""


def pattern(n):
    i = 1
    num = 1
    while i <= n:
        print(num, end=" ")
        num = num * 2
        i = i + 1
    print()


pattern(10)
