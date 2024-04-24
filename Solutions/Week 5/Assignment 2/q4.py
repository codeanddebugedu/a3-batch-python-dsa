# Method 1
def create_squares_dict():
    return {x: x**2 for x in range(1, 16)}


# Method 2
def create_squares_dict2():
    squares_dict = {}  # Initialize an empty dictionary
    for x in range(1, 16):  # Loop from 1 to 15
        squares_dict[x] = x**2  # Assign the square of x as the value for key x
    return squares_dict


ans = create_squares_dict2()
print(ans)
