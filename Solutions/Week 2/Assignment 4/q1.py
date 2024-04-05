"""
Create a function named divs, which will take two parameters n1 and n2. 
Return the count of how many numbers from 1 to n1 are divisible by n2
"""


def divs(n1: int, n2: int) -> int:
    i = 1
    count = 0
    while i <= n1:
        if i % n2 == 0:
            count += 1
        i += 1
    return count


print(divs(10, 2))
