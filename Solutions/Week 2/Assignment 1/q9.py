def check_number(number: int):
    if number > 0:
        print("positive")
    elif number < 0:
        print("negative")
    else:
        print("zero")


# Test cases
check_number(10)
check_number(-5)
check_number(0)
