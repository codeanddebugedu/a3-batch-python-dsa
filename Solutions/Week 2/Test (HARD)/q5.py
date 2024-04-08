"""
Make a function named sumOfFirstAndLastDigit which accepts an
integer n from the user. Calculate the sum of first and last digit of a
number and return it.
"""


def sumOfFirstAndLastDigit(num: int) -> int:
    if num <= 9:
        return num  # If num passed is less than 10
    n = num
    last_digit = n % 10
    while n > 0:
        if n <= 9:
            first_digit = n
            break
        n = n // 10
    return first_digit + last_digit


print(sumOfFirstAndLastDigit(1234))
print(sumOfFirstAndLastDigit(1000))
