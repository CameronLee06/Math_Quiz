import random

def yes_no(question):

    valid = False
    while not valid:
        response = input(question).lower()
            # strip removes white space before / after a string
        response = response.strip()

    if response== "yes" or response== "y":
        return "yes"

    elif response == "n" or response== "no":
        return "no"

    else:
        print("Please answer yes / no")

print("Welcome to the Ultimate Math Quiz!")
print()
print("Would you like to play?")
