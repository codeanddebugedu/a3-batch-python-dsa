# Create a function named sumOfSquares, which takes a single integer
# as a parameter named n. Return the sum of squares from 1 to n


def sumOfSquares(n):
    total = 0

    for i in range(1, n + 1):
        total += i**2

    return total


print(sumOfSquares(5))
