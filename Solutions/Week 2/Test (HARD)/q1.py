"""
Make a function named reverse which accepts an integer n from the
user. Reverse the number passed as a parameter and return the reverse
number. Do not use STRINGS.
"""


def reverse(num: int) -> int:
    n = num  # Do not change the original parameter
    result = 0
    while n > 0:
        last_digit = n % 10
        result = (result * 10) + last_digit
        n = n // 10
    return result


print(reverse(1000))
