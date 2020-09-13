""" The Basketball roster program """

# write a program that will build and display a basketball roster based off user input. Your program will then simulate an injury to a specific  player in the roster and prompt the user to update the roster. Upon updating the roster, your program will display the final roster and wish the newly added player good luck.

# print the welcome message
print("Welcome to the Basketball Roster program")

# create a empty list called roster
roster = []

# Get the user input for the names of the starting roster
point_guard = input("Enter the name of the Point Guard: ").title().strip()
roster.append(point_guard)
shooting_guard = input("Enter the name of the Shooting Guard: ").title().strip()
roster.append(shooting_guard)
small_forward = input("Enter the name of the Small Foward:").title().strip()
roster.append(small_forward)
power_forward = input("Enter the name of the  Power Foward:").title().strip()
roster.append(power_forward)
center = input("Enter the name of the Center").title().strip()
roster.append(center)

# print the starting 5 players of the roster.
print("\t Your starting 5 for the upcoming basketball season:")
print("\t\t Point Guard:\t\t" + str(roster[0]))
print("\t\t Shooting Guard:\t" + str(roster[1]))
print("\t\t Small Foward:\t\t" + str(roster[2]))
print("\t\t Power Foward:\t\t" + str(roster[3]))
print("\t\t Center:\t\t" + str(roster[4]))

# remove the injured player from the roster
injured_player = roster.pop(2)
print("\nOh no, " + str(injured_player) + " is injured")
print("Your roster has only " + str(len(roster)) + " players")

# take input for the new user
new_player = input("Who will take " + str(injured_player) + ":").title()
roster.insert(2, new_player)

# print the new roster
print("\t Your starting 5 for the upcoming basketball season:")
print("\t\t Point Guard:\t\t" + str(roster[0]))
print("\t\t Shooting Guard:\t" + str(roster[1]))
print("\t\t Small Foward:\t\t" + str(roster[2]))
print("\t\t Power Foward:\t\t" + str(roster[3]))
print("\t\t Center:\t\t" + str(roster[4]))

# closing greet
print("Good luck " + str(new_player) + " you will do great")
print(" Your roster now has " + str(len(roster)) + " players")

