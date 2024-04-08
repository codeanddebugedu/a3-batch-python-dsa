"""
Create a function named sumNum(), which takes 2 parameters as n1 and n2. 
Calculate and return the sum of all the numbers divisible by and 2 and 7 
between n1 to n2. Also if the sum is 0, then return -1
"""


def sumNum(n1: int, n2: int) -> int:
    total = 0
    for num in range(n1, n2 + 1):
        if num % 2 == 0 and num % 7 == 0:
            total += num

    if total == 0:
        return -1
    else:
        return total


print(sumNum(1, 30))
