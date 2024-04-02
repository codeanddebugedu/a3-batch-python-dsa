"""
Write a Python function to find the Maximum and minimum of three
numbers. Use 3 parameters. Make 2 different functions named as maxi and
mini.
"""


def maxi(a: float, b: float, c: float):
    if a >= b and a >= c:
        print(f"{a} is the maximum number")
    elif b >= c:
        print(f"{b} is the maximum number")
    else:
        print(f"{c} is the maximum number")


def mini(a: float, b: float, c: float):
    if a <= b and a <= c:
        print(f"{a} is the minimum number")
    elif b <= c:
        print(f"{b} is the minimum number")
    else:
        print(f"{c} is the minimum number")


num1: float = 10
num2: float = 5
num3: float = 8

maxi(num1, num2, num3)
mini(num1, num2, num3)
