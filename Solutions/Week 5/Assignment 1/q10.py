def student_marks():
    students = {
        "Alice": [95, 85, 90, 88, 93],
        "Bob": [75, 80, 78, 72, 70],
        "Charlie": [88, 90, 92, 85, 87],
        "Daisy": [65, 70, 68, 64, 67],
        "Ethan": [55, 57, 60, 58, 55],
    }
    results = {}
    for name, marks in students.items():
        total = sum(marks)
        percentage = total / 5
        print(f"Name = {name}, total = {total}, percentage = {percentage:.2f}")
    return results


student_marks()
