""" Rock paper scissors  """
# write program that will simulate playing the classic  game of Rock, Paper and Scissors againt computer AI. the program will ask the user how many rounds of the game they would like to play , simulate each round, keep score and determine an overall winner. The program will also print the classic phrases such as " Paper Covers rock" or " Scissors cut paper"

import random as r

# greet the user
print("Welcome to a game of Rock, Paper, Scissors")

# get the user input for how many rounds they would like to play and their name
name = input("\nWhat is your name:").strip().title()
rounds = int(input("\nHow many rounds would you like to play: "))

# create a variable to hold the player score and computer score and set it to 0
player_score = 0
computer_score = 0
moves = ["rock", "paper", "scissors"]

# play the game for the correct number of rounds specified by the user
for i in range( rounds):
    print(" \nRound: " + str(i+1))
    print(
        "\n"+str(name) + " : " + str(player_score) + "\t\t Computer: " + str(computer_score)
    )
    p_choice = input("Time to pick ....Rock , Paper, Scissors:").lower().strip()
    # after users move get the computer's move
    c_index = r.randint(0, 2)
    c_choice = moves[c_index]
    # here to make the random selection from the give list we do this step
    # where the index of the list is radomized and passed to the list

    # check if the player makes a valid move
    if p_choice in moves:
        print("\tComputer: " + c_choice)
        print("\t" + str(name) + ":" + p_choice)
        # now check for the various possible condtions for the game
        # if computer chooses rock
        if p_choice == "rock" and c_choice == "rock":
            winner = "tie"
            phrase = "It is a tie "
        elif p_choice == "paper" and c_choice == "rock":
            winner = str(name)
            phrase = "Paper covers rock"
        elif p_choice == "scissors" and c_choice == "rock":
            winner = "computer"
            phrase = "Rock break scissors"
        # if computer chosses paper
        elif p_choice == "rock" and c_choice == "paper":
            winner = "computer"
            phrase = "Paper covers rock"
        elif p_choice == "paper" and c_choice == "paper":
            winner = "tie"
            phrase = "It is a tie "
        elif p_choice == "scissors" and c_choice == "paper":
            winner = str(name)
            phrase = "Scissors cut paper"
        # if computer chooses scissors
        elif p_choice == "rock" and c_choice == "scissors":
            winner = str(name)
            phrase = "Rock break scissors"
        elif p_choice == "paper" and c_choice == "scissors":
            winner = "computer"
            phrase = "Scissors cut paper"
        elif p_choice == "scissors" and c_choice == "scissors":
            winner = "tie"
            phrase = "It is a tie "
        # catch for any other conditions
        else:
            print("Round winner not calculated")
            winner = "tie"
            phrase = "It is a tie, how boring!"
        # display the round results
        print("\t" + phrase)
        if winner == str(name):
            print("\tYou win round " + str(i+1) + ".")
            player_score += 1
        elif winner == "computer":
            print("\tComputer wins round " + str(i+1) + ".")
            computer_score += 1
        else:
            print("This round is a tie !")
    # else if the player didnot make a valid move
    else:
        print("That is not a valid game option !")
        print("Computer gets a point")
        computer_score += 1

# game has ended print the results 
print('\nFinal game results')
print("_-_-_-_-_-_-_-_-_-_-_-_")
print('\nRounds played:'+str(rounds))
print('Player score: '+str(player_score))
print('Computer score: '+str(computer_score))
# decide the winner based upon the scores above
if player_score>computer_score:
    print(" \nWinner: "+str(name) ,end="\n")
elif computer_score>player_score:
    print(" \nWinner:Computer ",end="\n")
else: 
    print(' The was a Tie! ',end="\n")


