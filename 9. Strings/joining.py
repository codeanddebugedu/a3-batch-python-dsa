my_list = ["abc", "y", 12, 55.55, "python", "tghb"]

# result = "".join(my_list)
# result = "z".join(i for i in my_list)
result = "".join(str(i) for i in my_list)
print(result)
