def fact_of_fact(n):
    f = count = 1
    for i in range(1, n + 1):
        f *= i
        count *= f
    return count
