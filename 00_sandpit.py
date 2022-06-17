ask_name = input("what is your name?")

try:
    ask_number = int(input("number"))    # replace with integer checker when integrating
except ValueError:
    print("you did not enter a number")
    ask_number = ""

print("hello {}, your favourite integer is {}".format(ask_name, ask_number))
print("hello {}, your favourite integer is {}".format(ask_number, ask_name))