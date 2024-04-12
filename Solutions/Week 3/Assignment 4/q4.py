"""
Make a list of your own. Calculate the length of that 
list without using len() function
"""

my_list = [54, 67, 1, 43, 67, 100, 45, 32, 74, 51, 40]

# length = 0
# for i in range(len(my_list)):
#     length += 1
# print(length)

length = 0
for num in my_list:
    length += 1
print(length)
