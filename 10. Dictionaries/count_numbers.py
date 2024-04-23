arr = [1, 4, 5, 5, 4, 6, 3, 1, 1, 1, 2, 9]
n = len(arr)
freq_map = dict()  # { }

for i in range(n):
    freq_map[arr[i]] = freq_map.get(arr[i], 0) + 1

for num in arr:
    freq_map[num] = freq_map.get(num, 0) + 1

print(freq_map)


# for i in range(n):
#     if arr[i] not in freq_map:
#         freq_map[arr[i]] = 1
#     else:
#         freq_map[arr[i]] = freq_map[arr[i]] + 1

# print(freq_map)
