marks: dict[str, int | str] = {
    "science": 78,
    "english": 91,
    "maths": 56,
    "hindi": 84,
}

# Update/Add
print(marks)
marks["maths"] = "dwadwadwadwad"
marks["xyz"] = 74
print(marks)

# Delete
del marks["science"]
print(marks)
