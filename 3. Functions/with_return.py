# def marks(m1, m2):
#     total = m1 + m2
#     return total


# print(marks(10, 70))


def marks(m1: int, m2: int) -> str:
    total = m1 + m2
    return f"Your marks is {total}"


print(marks(50, 60))
