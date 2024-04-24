def update_dict_values(d, factor):
    for key, value in d.items():
        if type(value) == int:
            d[key] = value * factor
    return d


ans = update_dict_values({"apple": "9", "banana": 8, "cherry": 7, "orange": 10}, 3)
print(ans)
