"""
AND
C1  C2  Result
F   F   F
F   T   F
T   F   F
T   T   T

OR
C1  C2  Result
F   F   F
F   T   T
T   F   T
T   T   T

NOT
"""

physics = 67
chemistry = 16
maths = 99

# print(physics > 33 and chemistry > 33)
# print(physics > 33 or chemistry > 33 and maths > 33)
# print(physics > 33 or xyz > 33)
# print(not physics >= 33)
print(not (not physics > 33 and not chemistry > 33))
# not (not T and not F)
# not (F and T)
# not F
# T
