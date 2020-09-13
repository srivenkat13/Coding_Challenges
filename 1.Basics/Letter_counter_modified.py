""" The modified letter counter app """

# unlike the first letter counter app it also asks the users whether they want to match the case of their letter or not 


# display welcome message to the user
print("Welcome to the letter counter app")

# Ask fot the name of the user
name = input("What is your name:").capitalize()

# greet the user
print("Hello," + name + "!")
print("I will count the number of times a word/letter occurs in the message")

# get the user input
message = input("Enter your message")

# get the user input for letter/word he wants to find occurence of
key = input("Enter the letter/word you want to count the occurence of:")

# get user choice for Matching the case of not
 
choice = input("Do you want to match the cases of the letter or word (y/n)").lower()

# make the distinction fo the choice given
if(choice=='y'):
    #print a choice which takes the case into consideration
    letter_count1=message.count(key)
    # print the response 
    print("\n" + name + " your message has " + str(letter_count1) + " " + key + "'s in it.")
else:
    #print a choice which doesnot take the case into consideration. i.e, make both message and key into lowercase
    letter_count2=message.lower().count(key.lower())
    #print the response
    print("\n" + name + " your message has " + str(letter_count2) + " " + key + "'s in it.")

print('\nThank you for using the letter counter app')