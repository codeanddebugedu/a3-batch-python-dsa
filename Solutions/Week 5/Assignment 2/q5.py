# Method 1
def filter_string_values(d):
    return {k: v for k, v in d.items() if isinstance(v, str)}


# Method 2
def filter_string_values2(d):
    filtered_dict = {}  # Initialize an empty dictionary
    for key, value in d.items():
        if type(value) == str:  # Check if the value is a string
            filtered_dict[key] = value  # Add it to the new dictionary
    return filtered_dict
