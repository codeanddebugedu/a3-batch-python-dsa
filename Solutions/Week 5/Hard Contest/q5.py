"""
Write a Python program to capitalize the first and last 
letters of each word in a given string.
"""


def capitalize_first_last_letters(str1):
    str1 = result = str1.title()
    result = ""
    for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
    return result[:-1]


print(capitalize_first_last_letters("python is a great language"))
print(capitalize_first_last_letters("delhi is best city with 0 AQI"))
