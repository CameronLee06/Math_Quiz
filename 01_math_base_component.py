from dis import Instruction
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

def instructions():
    print()
show_instructions = yes_no("would you like to see the instructions?") 
 
if show_instructions == "yes":
    instructions()

