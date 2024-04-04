"""
Create a function named div_by_3_and_5 which takes 2 integers as a
arguments (n1,n2), and print all the numbers divisible by 3 and 5 between
n1 and n2.
"""


def div_by_3_and_5(n1: int, n2: int):
    i: int = n1
    while i <= n2:
        if i % 3 == 0 and i % 5 == 0:
            print(i, end=" ")
        i += 1
    print()


div_by_3_and_5(10, 30)
div_by_3_and_5(1, 60)
