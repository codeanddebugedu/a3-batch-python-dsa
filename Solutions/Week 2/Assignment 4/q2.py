def isLeapYear(year: int) -> bool:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


i = 1
while i <= 2000:
    if isLeapYear(i):
        print(i, end=" ")
    i += 1
