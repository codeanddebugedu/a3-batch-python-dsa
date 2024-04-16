arr = [56, 2, 76, 32, 32, 32, 65, 89, 32, 78, 32, 32]
result = []
x = 32

for num in arr:
    if num != x:
        result.append(num)

print(result)
