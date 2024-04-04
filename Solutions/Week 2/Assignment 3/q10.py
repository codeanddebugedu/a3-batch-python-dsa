"""
Create a function named printPattern that takes one integer (num) as
an argument. Print from -num to num. Also keep in mind number passed as
an argument can be negative or positive.
"""


def printPattern(num: int):
    if num > 0:
        start: int = -num
        end: int = num
    else:
        start: int = num
        end: int = -num
    while start <= end:
        print(start, end=" ")
        start += 1
    print()


printPattern(-9)
