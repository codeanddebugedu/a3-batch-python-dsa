def numbers_sum(lst):
    sum = 0
    for i in lst:
        if type(i) == int:
            sum = sum + i
    return sum
