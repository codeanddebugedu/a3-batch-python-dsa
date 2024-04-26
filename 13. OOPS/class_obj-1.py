# in python every thing is object


class Student:
    # Attributes/Class Variables
    def __init__(self, id: int, name: str, gender="Female", age=0) -> None:
        self.id = id
        self.name = name
        self.gender = gender
        self.age = age

    def setDetails(self):
        self.id = int(input("Enter ID = "))
        self.name = input("Enter name = ")
        self.gender = input("Enter gender = ")
        self.age = int(input("Enter age = "))

    def displayName(self):
        print(f"Your name is {self.name}")

    def display(self):
        print(f"ID = {self.id}")
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")


s1 = Student(33, "Anirydh", "Male", 99)

s1.display()
