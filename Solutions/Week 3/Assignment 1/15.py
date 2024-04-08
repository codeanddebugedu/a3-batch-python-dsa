def longest_time(h, m, s):
    x = m // 60
    y = s // 3600
    if h > x and h > y:
        return h
    elif x > h and m > (s // 60):
        return m
    else:
        return s
