details = [
    {"name": "Anirudh", "age": 98, "gender": "Male"},  # <--x | x["age"]
    {"name": "Pratik", "age": 18, "gender": "Male"},
    {"name": "Muskan", "age": 32, "gender": "Female"},
    {"name": "Nihar", "age": 54, "gender": "Male"},
]

"""
Name = Anirudh, Age = 98, Gender = Male
"""

new_Details = sorted(details, key=lambda x: x["age"])
# print(details)
# print(new_Details)

for index in range(0, len(new_Details)):
    d = new_Details[index]
    if d["age"] >= 18:
        print(f"Name = {d['name']} , Age = {d['age']} , Gender = {d['gender']}")
