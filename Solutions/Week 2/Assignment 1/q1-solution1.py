"""
Write a Python function to find the Maximum and minimum of three
numbers. Use 3 parameters. Make 2 different functions named as maxi and
mini.
"""


def maxi(a: float, b: float, c: float):
    result = max(a, b, c)
    print(f"{result} is the max number")


def mini(a: float, b: float, c: float):
    result = min(a, b, c)
    print(f"{result} is the min number")


num1: float = 10
num2: float = 5
num3: float = 8

maxi(num1, num2, num3)
mini(num1, num2, num3)
