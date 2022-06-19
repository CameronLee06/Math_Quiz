import random
import math

colour = "blue"
item = "sky"

question = "is the {} {}".format(item, colour)
ask = input(question)
answer = "yes"

if ask == answer:
    print("yay")
else:
    print("awkward")