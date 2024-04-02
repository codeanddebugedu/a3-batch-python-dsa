"""
Function which takes one integer argument

Return a string, ODD, EVEN
"""


def even_odd_check(num: int) -> str:
    if num % 2 == 0:
        return "EVEN"
    # .....
    return "ODD"


ans = even_odd_check(61)
print(ans)
ans = even_odd_check(82)
print(ans)
