"""
Make a function named checkPalindrome which accepts an integer n
from the user. Return True or False if the number is palindrome or not.
Palindrome means which is same as forward and backwards. Do not use
STRINGS.
"""


def reverse(num: int) -> int:
    n = num
    result = 0
    while n > 0:
        last_digit = n % 10
        result = (result * 10) + last_digit
        n = n // 10
    return result


def checkPalindrome(num: int) -> bool:
    reversed_number: int = reverse(num)
    if reversed_number == num:
        return True
    else:
        return False


print(checkPalindrome(123321))
