"""
Create a dictionary that counts the frequency of words in a given string. 
Ask string from user.
"""


# Optimal Way
def wordFrequency(string: str):
    words = string.split()
    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1
    return frequency_dict


frequency = wordFrequency("python is is a good python good python")
print(frequency)
