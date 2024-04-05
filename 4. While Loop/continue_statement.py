"""
1
2
3
4
5
5
5
5
5
5...infinite
"""

i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1
