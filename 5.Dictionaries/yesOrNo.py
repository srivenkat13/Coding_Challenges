# yes or no polling app
# write a program that will conduct a poll on a yes or no issue.
# upon starting the program user will be prompte for and issue to vote on, the number of voters, and a password to view the poll results. Each time the user has voted the program asks to enter the user full name to ensure they voted or not.
# If the voter has not voted the user will be presented with the issue and can vote yes or no. The vote will be recorded. Once the number of voters specified by the user has been reached, the poll will close and the summary will be displayed. If the user enters the correct password a result of each voters name and  how they voted will be displayed.

# welcome message
print("Welcome to the voting app")

# get the user input for the yes or no they will be voting for.
issue = input("What is the yes or no issue you will be voting on today: ")

# get the user input for number of votes that will be allowed to vote
votes_count = int(input("What is the number of votes you will allow on the issue: "))

# get the user input for the password to be used while voting
password = input("Enter a password for polling results: ")

# define  a variable to count the number of yes's and no's
yes = 0
no = 0
# blank dictonary to hold the results
results = {}

# simulating the voting
for v in range(votes_count):
    name = input("Enter the name: ").lower()
    if name in results.keys():
        print(" You have already voted, cannot vote again.")
        v += 1
    else:
        print(" You have to vote on the issue, " + issue + ".")
        choice = input("Enter your vote, yes or no: ").strip().lower()
        if choice == "yes" or choice == "y":
            choice = "Yes"
            yes += 1
        elif choice == "no" or choice == "n":
            choice = "No"
            no += 1
        else:
            print("Invalid input!, voted used .")
        # adding the vote to dictonrary
        results[name] = choice
        print(
            "Thank you "
            + name
            + " ! Your vote of "
            + results[name]
            + " has been recorded"
        )

# show the vote results
total_votes = len(results.keys())
print("\n The Following " + str(total_votes) + " people voted:")
for key in results.keys():
    print(key)

# summarize the voting results
print("\n On the following issue: " + issue)
if yes > no:
    print("Yes wins ! " + str(yes) + " votes in yes " + str(no) + " votes in no")
elif no > yes:
    print("No wins !" + str(no) + " votes in no " + str(yes) + " votes in yes")
else:
    print(" It was a tie !" + str(no) + " votes to " + str(yes) + ".")

# allow the admin to see the actual votes
guess = input("\n To see the voting results enter the admin password: ")
if guess == password:
    for key, value in results.items():
        print("Voter: " + key.upper() + "\t\tvote:" + value)
else:
    print("Password was incorrect")

# end
print("Thank you !")

