"""
Truthy Falsy

int -> 0 (Falsy), 1,2,3,-1,-2 (Truthy)
float -> 0.0 (Falsy), 1.2, 2.8, 3.1, -1.111,-2.22, 0.003 (Truthy)
str -> "" (Falsy), "anirudh", " ", "!", "dw32" (Truthy)
"""

num = 10
print(num % 2)
if not num % 2:
    print("EVEN")
else:
    print("ODD")
