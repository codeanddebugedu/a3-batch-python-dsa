my_list = [
    ["Akul", 99],  # <---- x   |  x[0][-1]
    ["Akaz", 54],
    ["Prateek", 21],
    ["Anirudh", 45],
]


new_list = sorted(my_list, key=lambda x: x[0][-1])
print(my_list)
print(new_list)
