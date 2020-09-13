""" Grade Point Average Calculator App """
#  write a program that will collect any number of grades from a user. The program will sort these grades numerically from highest to lowest and calculate the grade point average of the user. The program will then ask for the average the user desires and calculate what the user muft get on thier next assignment to achieve that average.  lastly, the program will make a copy of the users grades and allow them to alter one of their previous grades to see how doing worse or better on an assignment would have chaned their overall average.

# greet the user
print("Welcome to the Average Calculator App")

# get the user input for their name
name = input("\nWhat is your name?").strip().title()

# get the user input for how many grades they would like to enter
length = int(input("\nHow many Grades do you like to enter: "))

# create and empty list to hold the grades of the user
grades = []

# get the user input for their grades
for r in range(length):
    grades.append(int(input("Enter the grade:")))

# sort the grades and print them
grades.sort(reverse=True)
print("\nGrades from Highest to lowest:")
for r in grades:
    print("\t" + str(r))

# calculate the average of all the grades  and round to two decimal places
average = sum(grades) / length
average = round(average, 2)

# display the grade summary for the user
print(name + "'s Grade Summary: ")
print("\t Total number of Grades: " + str(length))
print("\t Highest Grades: " + str(max(grades)))
print("\t Lowest Grades: " + str(min(grades)))
print("\t Average of Grades: " + str(average))

# prompt the user to enter the desired average
desired_average = float(input("\nWhat is your desired Average:"))
grade_req = desired_average * (length + 1) - sum(grades)
grade_req = round(grade_req, 2)

# wish the user good luck
print("\n Good luck " + str(name) + " !")
print(
    "You will need to get a "
    + str(grade_req)
    + " on your next assignment to earn a "
    + str(desired_average)
    + " average"
)

# make a copy of original grades and modify it
new_grades = grades[:]
print(
    "\nLets see what average could have been if you did better/ worse on an assignment  "
)
print("Your actual grades are: " + str(grades))
grade_change = int(input("What Grade would you like to change:"))
new_grades.remove(grade_change)
new_entry = int(
    input("What grade would you like to change " + str(grade_change) + " to: ")
)
new_grades.append(new_entry)

# sort the new grades and print
new_grades.sort(reverse=True)
print("\n The New Grades Sorted are: ")
for grade in new_grades:
    print("\t" + str(grade))

# calculate the new average
new_average = sum(new_grades) / length
new_average = round(new_average, 2)

# print the new grade summary
print(name + "'s  New Grade Summary: ")
print("\t Total number of Grades: " + str(length))
print("\t Highest Grades: " + str(max(new_grades)))
print("\t Lowest Grades: " + str(min(new_grades)))
print("\t Average of Grades: " + str(new_average))

# print a summary on how the average changed
print(
    " \n Your new average would be a "
    + str(new_average)
    + "Compared to your real average of "
    + str(average)
)
average_change = new_average - average
average_change = round(average_change, 2)
print("That is a change of " + str(average_change) + " points!")

# display the original grades
print("\nToo bad your original grades are still the same! ")
print(grades)
print("You should go ask for extra Credit!")
