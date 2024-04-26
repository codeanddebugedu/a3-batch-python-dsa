my_dictionary = {
    "science": 78,
    "english": 91,
    "maths": 56,
    "hindi": 84,
}

xyz = my_dictionary.copy()
print(id(my_dictionary))
print(id(xyz))
print(f"my_dictionary = {my_dictionary}")
print(f"xyz = {xyz}")
print("-------")

xyz["hindi"] = 100

print(f"my_dictionary = {my_dictionary}")
print(f"xyz = {xyz}")
