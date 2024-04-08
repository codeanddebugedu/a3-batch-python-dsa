def prime_numbers(num):
    cnt = 0
    for i in range(2, num):
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime:
            cnt += 1
    return cnt
