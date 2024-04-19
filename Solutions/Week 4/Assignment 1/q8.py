"""
Take 10 integer inputs from user and store them in a list. 
Now, copy all the elements in another list but in reverse order.
"""

from typing import List

my_list: List[int] = []

for i in range(10):
    num: int = int(input("Enter a number = "))
    my_list.append(num)

reverse_list = []

# Iterate the first list in reverse and append in reverse_list variable
for i in range(len(my_list) - 1, -1, -1):
    reverse_list.append(my_list[i])

print(reverse_list)
