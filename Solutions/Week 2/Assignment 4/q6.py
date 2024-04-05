"""
Don't create a function, just print the following pattern
1  11  111  1111  11111....n times (Ask n from user)
"""


def pattern(n):
    i = 1
    num = 1
    while i <= n:
        print(num, end=" ")
        num = (num * 10) + 1
        i = i + 1
    print()


# You can even directly ask number as given below
# Although it is not recommended but still you can.

# Best way is to ask input and store it in a variable
# and pass that variable to the function
pattern(int(input("Enter a number = ")))
