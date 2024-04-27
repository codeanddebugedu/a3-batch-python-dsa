def convertValues(data: list[dict]):
    for d in data:
        for key, value in d.items():
            if "." in value:
                d[key] = float(value)
            else:
                d[key] = int(value)
    return data


list1 = [
    {"x": "10", "y": "20", "z": "30"},
    {"p": "40", "q": "50", "r": "60"},
]

output1 = convertValues(list1)
print(output1)

list2 = [
    {"x": "10.12", "y": "20.23", "z": "30"},
    {"p": "40.00", "q": "50.19", "r": "60.99"},
]

output2 = convertValues(list2)
print(output2)
