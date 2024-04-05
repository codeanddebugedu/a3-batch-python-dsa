def evenTotal(start, end) -> int:
    total = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            total = total + i
    return total


s = int(input("Enter start number = "))
e = int(input("Enter end number = "))
print(evenTotal(s, e))
