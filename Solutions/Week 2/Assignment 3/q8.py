"""
Create a function named multiplicationTable that takes an integer
num as an argument. Print the multiplication table of that number up to 10
numbers.
"""


def multiplicationTable(num: int):
    i: int = 1
    while i <= 10:
        print(f"{num} X {i} = {num*i}")
        i += 1


multiplicationTable(231)
