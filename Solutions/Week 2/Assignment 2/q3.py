"""
Ask 3 numbers from user. Make a function which returns the middle of those 3 numbers.
Then make a function to check if that middle number is divisible by both 3 and 4. 
Make 2 functions for reusability.
"""


def findMiddleNumber(num1: int, num2: int, num3: int) -> int:
    if (num1 <= num2 <= num3) or (num3 <= num2 <= num1):
        return num2
    elif (num2 <= num1 <= num3) or (num3 <= num1 <= num2):
        return num1
    else:
        return num3


def isDivisibleBy3and4(number: int) -> bool:
    return number % 3 == 0 and number % 4 == 0  # This will directly return True/False


num1: int = int(input("Enter the first number: "))
num2: int = int(input("Enter the second number: "))
num3: int = int(input("Enter the third number: "))

middle_number: int = findMiddleNumber(num1, num2, num3)
print(f"The middle number is: {middle_number}")

if isDivisibleBy3and4(middle_number):
    print(f"{middle_number} is divisible by both 3 and 4.")
else:
    print(f"{middle_number} is not divisible by both 3 and 4.")
