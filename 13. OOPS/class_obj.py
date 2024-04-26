# in python every thing is object


class Student:
    # Attributes/Class Variables
    def __init__(self):
        self.id = int(input("Enter ID = "))
        self.name = input("Enter name = ")
        self.gender = input("Enter gender = ")
        self.age = int(input("Enter age = "))
        # self.school_name = "XYZ School"
        self.display()

    def displayName(self):
        print(f"Your name is {self.name}")

    def display(self):
        print(f"ID = {self.id}")
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")


s1 = Student()
print("----------")
s1.display()
