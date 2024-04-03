"""
start
end

even numbers -> total

1 to 10
2 4 6 8 10 -> 30


start = 71
end = 189
"""


def evenSum(start: int, end: int):
    i: int = start
    total: int = 0
    while i <= end:
        if i % 2 == 0:
            total = total + i
        i += 1
    return total


print(evenSum(71, 189))
