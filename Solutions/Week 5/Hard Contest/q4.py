"""
Convert Snake case to Pascal case.
"""

test_str = "we_are_learning_python_programming"
res = test_str.replace("_", " ").title().replace(" ", "")
print(res)
