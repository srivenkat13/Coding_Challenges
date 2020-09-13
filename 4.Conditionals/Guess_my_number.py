"""  Guess my number app """
# write a program that will play the classic " Hi Low " game. the program will randomly pick a number from 1 and 20. Users will then guess the number, with each guess,the program will either guess the number is too high or too low . When the user gussess correctly or after 5 guesses the program wikk end the game and summarize the results

import random as r

# greet the user
print("Welcome to the Guess my Number app")

name = input("Hello, What is your name: ").strip().title()

print(
    "Well "
    + str(name)
    + ", I'm Thinking of a number between 1 and 50.You have chances to guess "
)

# use the random library to generate a random integer between 1 and 25
number = r.randint(1, 50)

# check the number with user input in 5 guesses

for i in range( 5):
    yourNum = int(input("\nTake a guess: "))
    if yourNum > number:
        print("Your Guess is too high.")
    elif yourNum < number:
        print("Your Guess is too low .")
    else:
        break

# the hame is done, recap winning or loosing
if yourNum == number:
    print(
        "Good job " + str(name) + ", You guessed my number in " + str(i) + " guesses!"
    )
else:
    print("Game Over. The number I was thinking of was " + str(number) + ".")
