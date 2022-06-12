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

easy_mode = 0
medium_mode = 0
hard_mode = 0

choose_instruction = ("press <1> for easy, <2> for medium, <3> for hard")

# ask user for # of rounds, <enter> for infinite mode 


print()
print("what difficulty do you want to play on?")
print()

choose = input("{} or 'xxx' to end: ".format(choose_instruction))

print()

print("you chose {}".format(choose))

print()

if choose == "1":
    print("you are now playing on easy difficulty".format(easy_mode))

if choose == "2":
    print("you are now playing on medium difficulty".format(medium_mode))

elif choose == "3":
    print("you are now playing on hard difficulty".format(hard_mode))