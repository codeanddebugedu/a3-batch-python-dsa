# Method 1
def merge_dictionaries(d1, d2):
    merged = d1.copy()  # Copy the first dictionary
    merged.update(d2)  # Update with the second dictionary (overwrites if key exists)
    return merged


# Method 2
def merge_dictionaries2(d1, d2):
    merged = d1.copy()  # Start with a copy of the first dictionary
    for key, value in d2.items():
        merged[key] = (
            value  # Set the value from the second dictionary, overwriting if key exists
        )
    return merged


print(
    merge_dictionaries2(
        {"apple": 3, "banana": 5, "cherry": 7},
        {"banana": 8, "orange": 10, "apple": 9},
    )
)
