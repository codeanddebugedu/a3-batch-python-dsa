def bonus(days):
    total = 0
    for i in range(1, days + 1):
        if 32 < i <= 40:
            total += 325
        if 40 < i <= 48:
            total += 550
        if i > 48:
            total += 600
    return total
