# Pass by value -> int,floats,strings


def change(a: int, b: int):
    a = 100
    b = 100


a = 1
b = 1
change(a, b)
print(a)
print(b)
