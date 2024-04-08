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


def printPrimeFactors(num: int) -> None:
    i = 1
    while i <= num:
        if num % i == 0:
            if checkPrime(i):
                print(i, end=" ")
        i += 1
    print()


printPrimeFactors(20)
printPrimeFactors(7)
printPrimeFactors(72)
