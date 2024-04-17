# To create new lists
# result = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         result.append(i)

# print(result)

# start = 1
# end = 10
# result = ["EVEN" if i % 2 == 0 else "ODD" for i in range(start, end + 1)]
# result = [i for i in range(1, 11) if i % 2 == 0]
# print(result)
arr = ["567", "90", "541", "75", "96"]

result = [int(i) for i in arr]
print(result)
