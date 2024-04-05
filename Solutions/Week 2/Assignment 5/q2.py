"""
Write a program to display the n terms of a harmonic series and their sum.
1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n terms
Lets suppose n=5.
1/1 + 1/2 + 1/3 + 1/4 + 1/5 = 2.283334
"""


def harmonicSum(n: int) -> float:
    i: int = 1
    total: float = 0
    while i <= n:
        total = total + (1 / i)
        i += 1
    return total


print(harmonicSum(5))
print(harmonicSum(10))
