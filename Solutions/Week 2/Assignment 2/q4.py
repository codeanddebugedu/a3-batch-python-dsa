"""
Write a Python program that takes four numbers from the user. 
Implement a function to find the average of the first three numbers. 
Then, create another function to check if the average is greater than or equal to the fourth number. 
Make sure to use these two functions to determine and print whether the average 
is greater than or equal to the fourth number or not.
"""


def calculateAverage(num1: int, num2: int, num3: int) -> float:
    return (num1 + num2 + num3) / 3


def isAverageGreaterOrEqual(average: float, fourth_number: int) -> bool:
    return average >= fourth_number


num1: int = int(input("Enter the first number: "))
num2: int = int(input("Enter the second number: "))
num3: int = int(input("Enter the third number: "))
num4: int = int(input("Enter the fourth number: "))

average_value: float = calculateAverage(num1, num2, num3)

# Check if the average is greater than or equal to the fourth number
result = isAverageGreaterOrEqual(average_value, num4)

print(f"The average of {num1}, {num2}, and {num3} is: {average_value}")

if result:
    print(f"The average is greater than or equal to {num4}.")
else:
    print(f"The average is less than {num4}.")
