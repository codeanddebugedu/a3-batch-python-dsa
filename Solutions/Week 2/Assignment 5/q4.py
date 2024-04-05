def patterSum(x: int, n: int) -> float:
    i: int = 1
    total: float = 0
    y: int = 1
    while i <= n:
        if i % 2 != 0:
            total = total + (x**y)
        else:
            total = total - (x**y)
        y += 2
        i += 1
    return total


print(patterSum(6, 4))
print(patterSum(9, 11))
