"""
Ask a number from user. Print if that number is prime or not, use functions.
"""


def isPrime(n: int) -> None:
    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    if count == 2:
        print("Prime")
    else:
        print("Not Prime")


isPrime(10)
isPrime(7)
