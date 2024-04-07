"""
Make a function named printWords which accepts an integer n from
the user. Print the number as words.
"""


def reverse(num: int) -> int:
    n = num
    result = 0
    while n > 0:
        last_digit = n % 10
        result = (result * 10) + last_digit
        n = n // 10
    return result


def printWords(num: int) -> None:
    reversed_number = reverse(num)
    while reversed_number > 0:
        last_digit = reversed_number % 10
        if last_digit == 0:
            print("Zero", end=" ")
        elif last_digit == 1:
            print("One", end=" ")
        elif last_digit == 2:
            print("Two", end=" ")
        elif last_digit == 3:
            print("Three", end=" ")
        elif last_digit == 4:
            print("Four", end=" ")
        elif last_digit == 5:
            print("Five", end=" ")
        elif last_digit == 6:
            print("Six", end=" ")
        elif last_digit == 7:
            print("Seven", end=" ")
        elif last_digit == 8:
            print("Eight", end=" ")
        elif last_digit == 9:
            print("Nine", end=" ")
        reversed_number = reversed_number // 10
    print()


printWords(123)
printWords(100001)
