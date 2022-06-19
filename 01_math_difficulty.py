choose_difficulty = ("Press <E> for Easy, <M> for Medium or <H> for Hard")
easy_mode = 0
medium_mode = 0
hard_mode = 0

# ask user what difficulty they would like to play on, then let them choose

print()
print("What difficulty would you want to play on?")
print()

choose = input("{} or 'xxx' to end: ".format(choose_difficulty))

print()
print("You chose {}".format(choose))
print()

if choose == "E":
    print("you chose to play on easy dofficulty")

elif choose == "M":
    print("you are now playing on easy difficulty")

elif choose == "H":
    print("you are now playing on hard difficulty")