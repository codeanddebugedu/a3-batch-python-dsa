def sum_neg(nums):
    p, n = 0, 0
    if nums == []:
        return []
    else:
        for i in nums:
            if i > 0:
                p += 1
            else:
                n += i
        return [p, n]
