a = (54, 43, 11, 91, 92)
print(f"ID OF A = {id(a)}")
b = list(a)

b.append(100)
print(b)

a = tuple(b)
print(f"ID OF A = {id(a)}")
print(a)
