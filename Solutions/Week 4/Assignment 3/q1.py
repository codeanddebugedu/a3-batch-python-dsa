"""
Make a list of your own. Print the whole list in reverse using 
FOR loop and WHILE loop.
"""

my_list = [43, 65, "Elon", "Ambani", False, 55.43]

# for i in range(len(my_list) - 1, -1, -1):
#     print(my_list[i])

i = len(my_list) - 1
while i > -1:
    print(my_list[i])
    i -= 1
