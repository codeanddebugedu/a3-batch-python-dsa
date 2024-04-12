def unique(numbers):
    # Check each number in the list
    for i in range(len(numbers)):
        # Assume the current number is unique
        is_unique = True

        # Compare it against all other numbers
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                is_unique = False
                break

        # If no duplicates were found, this number is unique
        if is_unique:
            return numbers[i]


# Testing the function with examples
print(unique([3, 3, 3, 7, 3, 3]))  # ➞ 7
print(unique([0, 0, 0.77, 0, 0]))  # ➞ 0.77
print(unique([0, 1, 1, 1, 1, 1, 1, 1]))  # ➞ 0
