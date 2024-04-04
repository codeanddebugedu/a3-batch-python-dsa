def factors1(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
    print()


def factors2(n):
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            print(i)
            if n // i != i:
                print(n // i)
    print()


# factors1(3600000000)
factors2(360000000000000)
