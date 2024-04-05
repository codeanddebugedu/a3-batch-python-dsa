def patterSum(x: int, n: int) -> float:
    i: int = 1
    total: float = 0
    y: int = 1
    while i <= n:
        total = total + (x / y)
        y += 2
        i += 1
    return total


print(patterSum(6, 4))
