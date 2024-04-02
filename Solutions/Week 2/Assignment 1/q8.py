def simple_calculator(num1: float, num2: float, operation: str):
    if operation == "+":
        print(f"The result is: {num1 + num2}")
    elif operation == "-":
        print(f"The result is: {num1 - num2}")
    else:
        print("Unsupported operation")


# Test cases
simple_calculator(5, 3, "+")
simple_calculator(10, 4, "-")
simple_calculator(7, 2, "*")
