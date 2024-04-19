"""
Ask a string from user. Print the string with first 2 letters and last 2 letters.
"""


def printFirstAndLastTwoCh(string: str):
    if len(string) < 2:
        print("Not enough characters")
        return

    print(string[:2] + string[-2:])


printFirstAndLastTwoCh("code")
printFirstAndLastTwoCh("aeroplane")
printFirstAndLastTwoCh("c")
