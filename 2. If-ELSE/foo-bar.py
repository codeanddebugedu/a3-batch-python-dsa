# FOO-BAR
"""
User input (number)

Divisible by 3: FOO
Divisible by 5: BAR
divisible by 3 and 5 : FOOBAR
FOOFOOBARBAR

3 -> FOO
5 -> BAR
30 -> FOOBAR

14 -> FOOFOOBARBAR
"""
number: int = int(input("Enter number = "))
if number % 3 == 0 and number % 5 == 0:
    print("FOOBAR")
elif number % 3 == 0:
    print("FOO")
elif number % 5 == 0:
    print("BAR")
else:
    print("FOOFOOBARBAR")
