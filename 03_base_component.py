 
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
end = False

print("Welcome to the Ultimate Math Quiz!")
print()

show_instructions = yes_no("would you like to see the instructions?") 

# if user says "yes" to wanting to see instructions, display instructions 
if show_instructions == "yes":
    instructions()

questions_wanted = intcheck("How many questions do you want to be asked?: ", 1)

quiz_summary = []

end_quiz = "no"
while questions_asked < questions_wanted and end_quiz == "no":
    
    questions_asked += 1
    
    # generates a random number and question for user to attempt

    if questions_asked <= 10 | questions_asked >=10:
        choice = random.choice("+-")
        number_one = random.randint(1,20)
        number_two = random.randint(1,20)
        print(number_one, choice, number_two)
        answer = intcheck("Please answer the question with a number")

# checks if user got the addition question correct or not
    if choice == "+":
        actual_answer = number_one + number_two
        if answer == actual_answer:
            print ("")
            feedback = "!!!You got it correct!!!"
            correct_questions += 1

        else:
            print ("")
            feedback = ("^^^You got it incorrect^^^") 
            questions_incorrect += 1
            
# checks if user got the subtraction question correct or not    
    elif choice == "-":
        actual_answer = number_one - number_two
        if answer == actual_answer:
            print ("")
            feedback = "!!!You got it correct!!!"
            correct_questions += 1

        else: 
            print ("")
            feedback = "^^^You got it incorrect^^^"
            questions_incorrect += 1

    outcome = "Round {}: {}".format(questions_asked, feedback)
    print(feedback)
    print()
    quiz_summary.append(outcome)

    questions_correct = questions_asked - questions_incorrect

# **** Calculate Game Stats ******
percent_win = questions_correct / questions_asked * 100
percent_lose = questions_incorrect / questions_asked * 100

print()
print ("***** Game History *****")
for game in quiz_summary:
    print(game)

print()
# displays game stats with % values to the nearest whole number
print("******* Game Statistics *******")
print ("Win {}, ({:.0f}%) \nLoss: {}, " "({:.0f}%)".format(questions_correct,percent_win,questions_incorrect,percent_lose))

print("Thank you for playing")