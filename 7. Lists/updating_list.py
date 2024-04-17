my_list = [45, 56, 44, 23, 99, 11, "Anirudh", True]
print(f"My list = {my_list}")
print(f"My list id = {id(my_list)}")

my_list[0] = 100
my_list[-1] = 100
print(f"My list = {my_list}")
print(f"My list id = {id(my_list)}")
