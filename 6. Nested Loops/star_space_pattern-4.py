n = 8
if n % 2 == 0:
    addition = 1
else:
    addition = 2
for i in range(1, n // 2 + addition):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

for i in range(n // 2, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
