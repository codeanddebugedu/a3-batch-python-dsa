# Calculating the factorial of a given number using a while loop.
n = int(input("Enter a number: "))
factorial = 1

while n > 0:
    factorial *= n
    n -= 1

print(f"The factorial of the given number is: {factorial}")
