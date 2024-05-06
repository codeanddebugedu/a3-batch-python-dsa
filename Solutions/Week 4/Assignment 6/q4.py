from typing import List


def joinNumbers(numbers: List[int], char: str) -> str:
    return char.join(str(i) for i in numbers)


numbers = []
for i in range(1, 6):
    num = int(input(f"Enter number {i} = "))
    numbers.append(num)

c = input("Enter a character = ")

result = joinNumbers(numbers, c)
print(result)
