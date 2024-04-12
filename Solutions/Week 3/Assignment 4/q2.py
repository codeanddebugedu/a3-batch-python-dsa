"""
Make a list of your own. Print all the numbers divisible by 3 and 4 in that list.
"""

my_list = [54, 132, 76, 87, 231, 432, 765, 876, 2, 1, 11]

# for i in range(0, len(my_list)):
#     if my_list[i] % 3 == 0 and my_list[i] % 4 == 0:
#         print(my_list[i])

for i in my_list:
    if i % 3 == 0 and i % 4 == 0:
        print(i)
