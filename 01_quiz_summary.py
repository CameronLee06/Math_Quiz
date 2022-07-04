import random
import math

questions_incorrect = 0
questions_correct = 0
questions_asked = 0

feedback = "sorry you lose"
questions_incorrect += 1


game_summary = []

outcome = "Round {}: {}".format(questions_asked, feedback)
print(feedback)
print()
game_summary.append(outcome)

questions_correct = questions_asked - questions_incorrect

# **** Calculate Game Stats ******
percent_win = questions_correct / questions_asked * 100
percent_lose = questions_incorrect / questions_asked * 100


print()
print ("***** Game History *****")
for game in game_summary:
    print(game)

print()
# displays game stats with % values to the nearest whole number
print("******* Game Statistics *******")
print ("Win {}, ({:.0f}%) \nLoss: {}, " "({:.0f}%)".format(questions_correct,percent_win,questions_incorrect,percent_lose))

print("Thank you for playing")