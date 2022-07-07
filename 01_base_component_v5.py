 
import random
import math

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



def instructions():
    print(
        """
    **** How To Play****

    You will be randomly asked different questions and you can
    choose to be asked between 1 and 10 that are never the same.

    You will then attempt to answer each question and see how many you get correct.

    **** Good Luck!****
    """
    )
    return

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


# ***** Main Routine ******

# initialise variables, set up holding list for game history
questions_asked = 0 
questions_incorrect = 0
correct_questions = 0

questions_wanted = intcheck("How many questions do you want: ", 1)

quiz_summary = []

print("Welcome to the Ultimate Math Quiz!")
print()


end_quiz = "no"
while questions_asked < questions_wanted and end_quiz == "no":
    
    questions_asked += 1
    print("heading")
    input()




print()
print ("we are done")
