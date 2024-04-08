# Create a function named as checkPrime that takes an integer as an argument.
# Print YES if the number passed is a prime number else print NO.


def checkPrime(num: int) -> None:
    factors = 0
    i = 1
    while i <= num:
        if num % i == 0:
            factors += 1
        i += 1
    if factors == 2:
        print("Yes")
    else:
        print("No")


checkPrime(7)
checkPrime(8)
