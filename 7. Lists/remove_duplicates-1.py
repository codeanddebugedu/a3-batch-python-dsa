def remove_duplicates(arr):
    result = []
    n = len(arr)
    for i in range(0, n):
        if arr[i] not in result:
            result.append(arr[i])
    return result


arr = [1, 3, 3, 2, 4, 1, 1, 2, 2, 3, 1, 4, 4, 4]
ans = remove_duplicates(arr)
print(ans)
