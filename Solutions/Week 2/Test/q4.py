# Make a function named factorial(), which takes an integer n.
# Return the factorial of that number


def factorial(n: int) -> int:
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


print(factorial(5))
