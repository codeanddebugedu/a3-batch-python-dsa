"""
Keep asking numbers from user until the user enters 0. 
Then display the average of all numbers.
"""


def average():
    total = 0
    count = 0
    while True:
        num = int(input("Enter a number = "))
        if num == 0:
            break
        total = total + num
        count = count + 1
    print(f"Average of all the numbers = {total/count}")


average()
