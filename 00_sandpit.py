import random 
import math


end = False
questions_asked = 0
correct_questions = 0

while end == False:
    if questions_asked <= 10 | questions_asked >=10:
        choice = random.choice("+-")
        number_one = random.randint(1,20)
        number_two = random.randint(1,20)
        print(number_one, choice, number_two)
        answer = int(input("please answer the question"))