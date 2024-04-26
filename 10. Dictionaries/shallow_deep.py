import copy

my_dictionary = {
    "science": 78,
    "english": 91,
    "gender": ["Male", "Female"],
}

# xyz = my_dictionary.copy()
# xyz = copy.copy(my_dictionary)  # Shallow Copy
xyz = copy.deepcopy(my_dictionary)  # Deep Copy

print(id(my_dictionary["gender"]))
print(id(xyz["gender"]))


xyz["gender"][0] = "gg"


print(f"my_dictionary = {my_dictionary}")
print(f"xyz = {xyz}")
