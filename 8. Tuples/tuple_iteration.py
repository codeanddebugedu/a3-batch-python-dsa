my_tuple = (54, 13, 5, 435, 346, 5, 2312, 3432)


print(my_tuple[0])
print(my_tuple[-1])

# Via index
for i in range(0, len(my_tuple)):
    print(my_tuple[i], end=" ")

print()
# Via Value
for num in my_tuple:
    print(num, end=" ")
