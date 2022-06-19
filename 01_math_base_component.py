import random

# yes no checker, make sure anything but "yes" "y" "n" or "no" is entered to continue
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

# checks user input is valid based on a list
def choice_checker(question, valid_list, error):
    print(question)
    error = "Please choose from easy / medium / hard (or xxx to quit)"

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()


        # Iterates through list and if response is an item
        # in the list (or the first letter of an item), the 
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
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

choose_difficulty = ("Press <E> for Easy, <M> for Medium or <H> for Hard")
easy_mode = 0
medium_mode = 0
hard_mode = 0

# ask user what difficulty they would like to play on, then let them choose

print()
print("What difficulty would you want to play on?")
print()

choose = input("{} or 'xxx' to end. !(capital sensitive)!:".format(choose_difficulty))

print()
print("You chose {}".format(choose))
print()

if choose == "E":
    print("you chose to play on easy difficulty")

elif choose == "M":
    print("you are now playing on medium difficulty")

elif choose == "H":
    print("you are now playing on hard difficulty")

print()
print("Question 1:")
print()

