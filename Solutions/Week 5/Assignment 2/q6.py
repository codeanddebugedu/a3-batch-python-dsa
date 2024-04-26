def max_char_frequency(s):
    freq = {}

    # Count each character's frequency
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Initialize variables to track the maximum frequency character
    max_char = None
    max_freq = 0

    # Iterate through the frequency dictionary to find the character with the highest frequency
    for char, count in freq.items():
        if count > max_freq:
            max_freq = count
            max_char = char

    # Display the character with the highest frequency
    print(f"The character with the maximum frequency is '{max_char}'")


max_char_frequency("heeellllllloo")
