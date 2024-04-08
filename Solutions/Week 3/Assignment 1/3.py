def calculate_exponent(num, exp):
    total = num
    for x in range(1, exp):
        total *= num
    return total
