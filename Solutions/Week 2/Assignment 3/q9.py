"""
Create a function named calSum which takes an 2 integer (n1 and n2)
as an argument. Calculate the sum of all the numbers divisible by 5
between n1 and n2 and return that sum. (Make sure that n1 is less than n2).
"""


def calSum(n1: int, n2: int) -> int:
    total: int = 0
    i: int = n1
    while i <= n2:
        if i % 5 == 0:
            total = total + i
        i += 1
    return total


ans = calSum(43, 68)
print(ans)
