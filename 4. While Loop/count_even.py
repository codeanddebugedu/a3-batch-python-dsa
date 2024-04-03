"""
start
end

Print how many even numbers are there
"""


def countEven(start, end):
    i = start
    count = 0
    while i <= end:
        if i % 2 == 0:
            count = count + 1
        i += 1
    return count


print(countEven(1, 22))
print(f"Number of even numbers = {countEven(1, 22)}")

x = countEven(45, 99)
print(x)
