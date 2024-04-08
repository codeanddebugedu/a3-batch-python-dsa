# Print all the prime numbers between 1 to 100.


def checkPrime(num: int) -> bool:
    factors = 0
    i = 1
    while i <= num:
        if num % i == 0:
            factors += 1
        i += 1
    if factors == 2:
        return True
    else:
        return False


def printPrimeInRange(n1, n2):
    for i in range(n1, n2 + 1):
        if checkPrime(i) == True:
            print(i, end=" ")
    print()


printPrimeInRange(1, 100)
