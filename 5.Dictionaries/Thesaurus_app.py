""" Thesaurus App """
# Write a program that will simulate a thesaurus, and will present a user with a list of words that your thesaurus contains. Based on the users choice, you will randomly display them with a synonym for their choosen word. Lastly, the program will display all the potential synonyms for each word in the thesaurus

import random as r

# create a dictionary called thesaurus
thesaurus = {
    "hot": ['balmy',' summery','tropical','boiling' ,'scorching'],
    "cold": ['chilly','cool','freezing','frigid','polar'],
    "happy": ['jubilant','ecstatic','cheerful','pleased','effervecense'],
    "sad": ['poignant','melancholy','miserable','downcast','unhappy'],
}

# greet the user
print("Welcome to the Thesaurus app")
# print the key of the thesaurus you got
print("\nChoose a word from the Thesaurus and I will give you the meaning ")
print("\n Here are the words in my thesaurus :")
for key in thesaurus.keys():
    print("\t-" + key.title())

# get the user input for the word of their choice
choice = input("\n What word would you like a synonym for : ").lower().strip()

# provide a random synonym from the dictionary
if choice in thesaurus.keys():
    index = r.randint(0, 4)
    print(" A synonym for " + choice + " is " + thesaurus[choice][index] + ".")
else:
    print("Sorry, the word is currently not in the Thesaurus. ")

# get the user to see whole thesaurus
see_thesaurus = (
    input("\n Would you like to see the whole thesaurus (yes/no )").lower().strip()
)

# show all the values of thesaurus
if see_thesaurus == "yes":
    for key, values in thesaurus.items():
        print("\n " + key.title() + " synonyms are :")
        for value in values:
            print("\t-" + value)
else:
    print("\n I hope you enjoyed the program. Thank you!")

