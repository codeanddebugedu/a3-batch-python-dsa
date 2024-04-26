a = "hello world"
print(len(a))

# Via Index
# for index in range(0, len(a)):
#     print(a[index])

# # Via Value
# for ch in a:
#     print(ch)

for index in range(len(a) - 1, -1, -1):
    print(a[index])
