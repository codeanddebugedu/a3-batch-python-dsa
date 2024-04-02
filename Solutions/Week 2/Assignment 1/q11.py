def calculate_interest(principal: float, rate: float, time: float):
    interest = (principal * rate * time) / 100
    print(f"The simple interest is: {interest}")


# Test cases
calculate_interest(1000, 5, 1)
calculate_interest(500, 7, 3)
calculate_interest(1500, 4.5, 6)
