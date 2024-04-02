"""
Attempt the same leap year question (Week 1 - Assignment 2 - Q8) but
using function. Try calling function with different years as a parameter and
check the output.
"""


def checkLeapYear(year: int):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")


checkLeapYear(2000)
checkLeapYear(2001)
