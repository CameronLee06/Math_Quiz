 
import random
import math

# checks for yes/no
def yes_no(question):

    valid = False
    while not valid:
        response = input(question).lower()

        # strip removes white space before / after a string
        response = response.strip()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "n" or response == "no":
            return "no"

        else:
            print("Please answer yes / no")


#asks user if they want to see the instructions
def instructions():
    print(
        """
    **** How To Play ****

    You will start by choosing 2 numbers of your choice to guess between.

    Then the computer will choose a number at random between your 2 chosen numbers.

    You will then have a specific amount of guesses ranging from how big the difference in your 2 numbers is.

    You will guess a number and the computer will say either higher or lower to get you closer to your number.


    ****Good Luck!****
        """
    )
    return ""



# ***** Main Routine ******



print("Welcome to the Ultimate Math Quiz!")
print()


for item in range(0,5):
    show_instructions = yes_no("would you like to see the instructions?") 

    # if user says "yes" to wanting to see instructions, display instructions 
    if show_instructions == "yes":
        instructions()

    print("Quiz starts...")


