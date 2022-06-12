import random

difficulty = ["Easy", "Medium", "Hard"]
for item in range (0,20):
    answer = random.choice(difficulty)
    print(answer)