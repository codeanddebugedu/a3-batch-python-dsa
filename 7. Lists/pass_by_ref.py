# Pass by reference, (address)
# Mutable


def change(a):
    print(f"Mylist = {id(a)}")
    a[0] = 100


xyz = [34, 22, 11, 78, 67, 65]
print(f"XYZ = {id(xyz)}")
change(xyz)
print(f"XYZ = {id(xyz)}")
print(xyz)
