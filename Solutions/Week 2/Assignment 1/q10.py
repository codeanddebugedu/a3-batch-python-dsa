def is_odd_even(number: int):
    if (number // 2) * 2 == number:
        print("Even")
    else:
        print("Odd")


# Test cases
is_odd_even(2)
is_odd_even(3)
is_odd_even(100)
