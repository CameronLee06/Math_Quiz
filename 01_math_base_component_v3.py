import random
import math


def getValue():
    userInput = ''
    try:
        userInput = int(input())
    except ValueError:
        return "retry"
    else:
        return userInput

userEntry = getValue()

while userEntry == 'retry':
    print("You entered a letter. Please put in a number.")
    userEntry = getValue()

print("You entered:",userEntry)


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
    
# Number checking function goes here
def intcheck(question, low=None, high=None, exit_code = None):

    while True:

        # sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between {} and {} (inclusive)".format(low, high)
        elif low is not None and high is None:
            error = "Please enter an integer that is more than or equal to {}".format(low)
        elif low is None and high is not None:
            error = "Please enter an integer that is less than or equal to {}".format(high)
        else:
            error = "Please enter an integer"

        try:
            response = input(question)
            
            # check to see if response is the exit code and return it
            if response == exit_code:
                return response
            
            # change the response into an integer
            else:
                response = int(response)

            # Checks response is not too low, not use of 'is not' keywords
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        # checks input is a integer
        except ValueError:
            print(error)
            continue


# ***** Main Routine *****
print("Welcome to the Ultimate Math Quiz!")
print()

show_instructions = yes_no("would you like to see the instructions?") 

# if user says "yes" to wanting to see instructions, display instructions 
if show_instructions == "yes":
    instructions()

# Ask user for # of rounds..
rounds = intcheck("How many questions would you like to be asked?", 1, )
print()

print("Question 1:")
print()

end = False
questions_asked = 0
correct_questions = 0
incorrect_questions = 0

# generates a random number and question for user to attempt
while end == False:
    if questions_asked <= 10 | questions_asked >=10:
        choice = random.choice("+-")
        number_one = random.randint(1,20)
        number_two = random.randint(1,20)
        print(number_one, choice, number_two)
        answer = int(input("please answer the question"))

# checks if user got the addition question correct or not
    if choice == "+":
        actual_answer = number_one + number_two
        if answer == actual_answer:
            print ("congrats, you got it")
            correct_answers = 1

        else:
            print ("Sorry you got it wrong")
    
# checks if user got the subtraction question correct or not    
    elif choice == "-":
        actual_answer = number_one - number_two
        if answer == actual_answer:
            print ("congrats, you got it")
            correct_answers = 1

        else: 
            print ("sorry, you got it wrong")
