# Attempt Week 1 - Assignment 2 (Q6) using function


def smallestNumber(num1, num2, num3, num4):
    smallest_number = num1

    if num2 < smallest_number:
        smallest_number = num2

    if num3 < smallest_number:
        smallest_number = num3

    if num4 < smallest_number:
        smallest_number = num4

    print(f"Smallest number = {smallest_number}")


smallestNumber(4, 3, 2, 1)
smallestNumber(5, 8, 2, 6)
