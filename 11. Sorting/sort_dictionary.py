# dict_items([('physics', 56), ('chemistry', 19),
# ('maths', 91), ('algebra', 74), ('history', 74)])

details = {
    "physics": 56,  # ('physics', 56) <---x | x[1]
    "chemistry": 19,
    "maths": 91,
    "history": 74,
    "algebra": 74,
}
# .......
new_details = dict(sorted(details.items(), key=lambda x: x[1]))
print(details)
print(new_details)
