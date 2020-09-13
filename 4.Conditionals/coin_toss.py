import random as r


""" The Coin Toss App """

# Write a program that will simulate the flipping a coin n number of times, the program will present the option to see the result i=of each individual flip. Your program will also inform the user any time the number of heads are equal to the number of tails flipped. Upon Completion of all the flips, your program will provide a summary table that shows the number and percentage of each flip..

# greet the user
print("Welcome to the Coin Toss App")
print("\nI will flip a coin a set number of times.")

count = int(input("How many times would you like to flip the coin: "))

choice = (
    input("Would you like to see the result of each indiviual flip of coin??(y/n) ")
    .strip()
    .lower()
)
print("\n Flipping .....\n")

# variables to store number of times heads and tails are flipped.
heads = 0
tails = 0

# The main for loop

for flip in range(count):
    # create the coin object
    coin = r.randint(0, 1)

    if coin == 1:
        heads += 1
        if choice.startswith("y"):
            print("HEADS")
    else:
        tails += 1
        if choice.startswith("y"):
            print("TAILS")
    if heads == tails:
        print(
            "At "
            + str(flip + 1)
            + " flips, the number of heads and tails were equal at "
            + str(heads)
            + " each"
        )

# calculate the percentages
heads_percentage = round(100 * heads / count, 2)
tails_percentage = round(100 * tails / count, 2)

#printing the results
print('\n\n Results of FLipping a Coin '+ str(count)+" times: ")
print('\n Side \t\t count\t\t percentage')
print('\n ---- \t\t -----\t\t ---------')

print('Heads\t\t'+str(heads)+"/"+str(count)+"\t\t"+str(heads_percentage)+"%")
print('Tails\t\t'+str(tails)+"/"+str(count)+"\t\t"+str(tails_percentage)+"%")
