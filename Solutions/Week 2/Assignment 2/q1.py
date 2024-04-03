"""
None is a special datatype in python

You can even store None in a variable and print its type.

a = None
print(a)
print(type(a))
"""


# Without Annotations
def largest(num1=None, num2=None, num3=None) -> int:
    if num1 != None and num2 != None and num3 != None:
        if num1 > num2 and num1 > num3:
            return num1
        elif num2 > num1 and num2 > num3:
            return num2
        else:
            return num3
    else:
        return -1


# With Annotations
# int | None --- It means it can be an int or None
def largest_part2(
    num1: int | None = None, num2: int | None = None, num3: int | None = None
) -> int:
    if num1 != None and num2 != None and num3 != None:
        if num1 > num2 and num1 > num3:
            return num1
        elif num2 > num1 and num2 > num3:
            return num2
        else:
            return num3
    else:
        return -1


print(largest(3, 4, 1))  # Output 4
print(largest())  # Output -1
