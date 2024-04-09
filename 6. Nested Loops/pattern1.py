"""
n=10
*
* *
* * *
* * * *
* * * * *
"""

n = 3
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
