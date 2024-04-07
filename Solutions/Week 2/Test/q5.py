"""
Might not be the best solution but easy to understand
"""


def factorial(n: int) -> int:
    i = 1
    answer = 1
    while i <= n:
        answer = answer * i
        i += 1
    return answer


def sumPattern(n: int) -> float:
    i = 1
    total = 0
    while i <= n:
        total = total + (1 / factorial(i))
        i += 1
    return total


print(sumPattern(5))
