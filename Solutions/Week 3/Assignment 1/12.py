def evenly_divisible(a, b, c):
    s = 0
    for i in range(a, b + 1):
        if i % c == 0:
            s += i
    return s
