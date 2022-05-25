import random

# yes no checker, make sure anything but yes no is entered to continue
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

# ask user if they would like to see the instructions or go straight to game
def instructions():
    print(
        """
    **** How To Play****

    You will start by choosing a difficulty (Easy, Medium, Hard).

    Then you will be randomly asked 10 different question that are never the same.

    You will then attempt to answer each question and see how many you get correct.

    **** Good Luck!****
    """
    )
    
show_instructions = yes_no("would you like to see the instructions?") 
 
if show_instructions == "yes":
    instructions()
    

