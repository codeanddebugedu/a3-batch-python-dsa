"""
Make a function named checkArmstrong which accepts an integer n
from the user. Return True or False if that number is an armstrong number.
"""


def checkArmstrong(num: int) -> bool:
    n = num
    total = 0
    while n > 0:
        last_digit = n % 10
        total = total + (last_digit**3)
        n = n // 10
    if total == num:
        return True
    else:
        return False


print(checkArmstrong(153))
print(checkArmstrong(407))
