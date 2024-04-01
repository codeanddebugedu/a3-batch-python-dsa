"""
ELIF
marks=95

91 to 100 -> A
81 -> 90 -> B
71 -> 80 -> C
61 -> 70 -> D
60 down -> FAIL
"""

marks = 95
if marks >= 91 and marks <= 100:
    print("A")
elif marks >= 81 and marks <= 90:
    print("B")
elif 71 <= marks <= 80:
    print("C")
elif marks >= 61 and marks <= 70:
    print("D")
elif marks >= 0 and marks <= 60:
    print("FAIL")
else:
    print("Invalid")
