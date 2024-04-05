"""
Create a function addDigits() that takes an integer as an argument. 
Calculate the sum of digits of that number.
"""


def addDigits(num: int) -> int:
    # Dont change the num so storing number in n
    n: int = num
    total = 0
    while n > 0:
        total = total + (n % 10)  # n%10 gives us last digit
        n = n // 10
    return total


print(addDigits(123))
print(addDigits(58714))
