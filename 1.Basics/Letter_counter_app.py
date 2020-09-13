""" THE LETTER COUNTER APP """

# You are responsible for writing a program that will get a message and a specific letter from a user and then count the number of occurrences of that letter in the given message. You program should count “H” and “h” as an occurence of h. Your program will then display a message to the user stating the occurrences of the given letter.

""" Welcome text """
print("Welcome to the letter counter app")

# getting the user input
user = input("What is your Name:").title().strip()
print("Hello, " + user + "!")

print("I will count the number of times that a specific letter/word occurs in a message")

# get the user message and covert it to lower case simultaenously to make sure 'h' and 'H' count as same.
msg = input("Please enter a message:").lower()

# get the user information for the letter they want to count
letter = (
    input("which letter/word would you like to count the occurrences of:").lower().strip()
)

# create a variable called letter count to store the occurrences of the given lettter
letter_count = msg.count(letter)

# end result stating the occurances of the asked letter
print(
    "\n" + user + " your message has " + str(letter_count) + " " + letter + "'s in it."
)
