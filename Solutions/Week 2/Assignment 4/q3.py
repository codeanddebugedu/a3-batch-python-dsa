"""
Create a function named factorial which takes a integer as an input
and returns the factorial of that number.
"""


def factorial(n):
    result = 1
    i = 1
    # I have iterate from 1 to n
    # If you want you can iterate from n to 1
    while i <= n:
        result = result * i
        i += 1
    return result


result = factorial(5)
print(result)
