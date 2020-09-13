"""  Voter Registration """

# Write a program that willl registration to vote. If the user is 18 or older, your program will present them with a list of potential political parties to regsiter for. Upon choosing a party, your program will confirm that the suer has registered and print a specific message depending on that party joined

# greet the user
print("Welcome to the Voter Registration App")

# get the user input for their name and age
name = input("Please Enter your name: ").strip().title()
age = int(input("Please enter your age: "))

# create the list that holds political parties
parties = ["Republican", "Democratic", "Independent", "Libertarian", "Green"]

# confirm the user age
if age >= 18:
    print(
        "Congratulations " + str(name) + "!" + "You are old enough to register to vote."
    )
    print("\n Here is a list of political parties to join. ")
    # print the list of parties
    for party in parties:
        print("\t\t-" + str(party))

    # take the user input for their party
    my_party = input("What party would you like to join:").title().strip()

    if my_party in parties:
        print(
            "Congratulations "
            + str(name)
            + "!"
            + "You have joined "
            + str(my_party)
            + " party !"
        )
        if my_party == "Republican" or my_party == "Democratic":
            print("That is a major party")
        elif my_party == "Independent":
            print("That is an idependent party")
        elif my_party == "Libertarian" or my_party == "Green":
            print("That is not a major party")
    else:
        print("The party you choose is not in the list")
# print that the user is below the age limit
else:
    print("Your not old enough to register to vote")

