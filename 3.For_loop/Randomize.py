""" Write a program In which the user gives a question to the CLI and gets a predefined random response from the program, and this should continue untill the user quits i.e. by hitting the enter twice. Hitting the enter once should let the user ask next question """

# the program needs random and sys modules to work with randomizing the output

import sys as s
import random as r

# importing both modules

answers = [
    "YES, DEFINETLY!!!",
    "IT'S CERTAIN..",
    "YOU MAY RELY ON IT!",
    "AS I SEE IT, YES!!!",
    "OUTLOOK LOOKS GOOD...",
    "MOST LIKELY...",
    "IT IS DECIDED SO...",
    "WITHOUT A DOUBT!!",
    "SERIOUSLY, FORGET IT !!" "EVEN GOD CANNOT HELP" "ITS BEYOND MY ABILITY",
]
# give the replies you want to display randomly in this file


# this to run the program continously
key = True
while key:
    User_input = input("Hello, Fortune teller here. Ask your Question...")
    output = r.choice(answers)
    # choice() function from the random modules picks any item from the given list or set or tuple , randomly
    if User_input == "":
        s.exit()
        # the program should end when the user hits enter without giving input , so this conditon
    elif User_input == " ":
        print("You need to enter some Question first")
        # this will be printed if at all the user gave blank input
    else:
        print(output)
        # in all the reamining cases there will be some output generated according to the choice function above.


""" ADD AS MANY ANSWERS AS YOU LIKE IN THE answer VARIABLE TO MAKE IT MORE FUN """
