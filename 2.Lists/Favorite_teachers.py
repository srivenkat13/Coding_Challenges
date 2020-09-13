""" Favorite teacher program """

# write a program that will create a list of user's favorite teachers. It will display these teachers ranked ( rank as they enter the list). Also display the list , alphabetically, in reverse alphabetical order, the top two teachers, the next two teachers. the last favorite tracher and the total number of favorite teachers in the list . The program will add and remove the teachers from the list each time displaying the summary...

# welcome message
print("Welcome to the favorite teacher app")

# create a blank list called favorite teachers
fav_teachers = []

# get the user input for his/her favorite user
fav_teachers.append(input("\nWho is your First Favorite teacher:").title())
fav_teachers.append(input("Who is your Second Favorite teacher:").title())
fav_teachers.append(input("Who is your Third Favorite teacher:").title())
fav_teachers.append(input("Who is your Fourth Favorite teacher:").title())

# print favorite teacher ranked, alphabetically sorted and reverse alphabetically sorted are
print("\nYour Favorite Teachers ranked are:" + str(fav_teachers))
print("Your Favorite Teachers Alphabetically sorted are:" + str(sorted(fav_teachers)))
print(
    "Your Favorite Teachers Reverse alphabetically sorted are:"
    + str(sorted(fav_teachers, reverse=True))
)

# summary
print(
    "Your top two favorite teachers are: "
    + str(fav_teachers[0])
    + " and "
    + str(fav_teachers[1])
)
print(
    "Your next two favorite teachers are: "
    + str(fav_teachers[2])
    + " and "
    + str(fav_teachers[len(fav_teachers) - 1])
)
print("Your last favorite teachers is: " + str(fav_teachers[len(fav_teachers) - 1]))
print("You have total " + str(len(fav_teachers)) + " Favorite teacher")

# remove the first favorite teacher from the list
print("\nOops, " + str(fav_teachers[0]) + " is no longer your first favorite teacher ")
fav_teachers.insert(0,input("Who is your new FAVORITE teacher: ").title())

# print favorite teacher ranked, alphabetically sorted and reverse alphabetically sorted are
print("\nYour Favorite Teachers ranked are:" + str(fav_teachers))
print("Your Favorite Teachers Alphabetically sorted are:" + str(sorted(fav_teachers)))
print(
    "Your Favorite Teachers Reverse alphabetically sorted are:"
    + str(sorted(fav_teachers, reverse=True))
)

# summary
print(
    "Your top two favorite teachers are: "
    + str(fav_teachers[0])
    + " and "
    + str(fav_teachers[1])
)
print(
    "Your next two favorite teachers are: "
    + str(fav_teachers[2])
    + " and "
    + str(fav_teachers[3])
)
print("Your last favorite teachers is: " + str(fav_teachers[len(fav_teachers) - 1]))
print("You have total " + str(len(fav_teachers)) + " Favorite teacher")


# user no longer likes his favorite teachers, ask the user to pick one name to remove from the list.
fav_teachers.remove(
    input(
        " \n You've decided you no longer like a teacher. Which teacher would you like to remove from you list: "
    ).title().strip()
)

# print favorite teacher ranked, alphabetically sorted and reverse alphabetically sorted are
print("\nYour Favorite Teachers ranked are:" + str(fav_teachers))
print("Your Favorite Teachers Alphabetically sorted are:" + str(sorted(fav_teachers)))
print(
    "Your Favorite Teachers Reverse alphabetically sorted are:"
    + str(sorted(fav_teachers, reverse=True))
)

# summary
print(
    "Your top two favorite teachers are: "
    + str(fav_teachers[0])
    + " and "
    + str(fav_teachers[1])
)
print(
    "Your next two favorite teachers are: "
    + str(fav_teachers[2])
    + " and "
    + str(fav_teachers[3])
)
print("Your last favorite teachers is: " + str(fav_teachers[len(fav_teachers) - 1]))
print("You have total " + str(len(fav_teachers)) + " Favorite teacher")
