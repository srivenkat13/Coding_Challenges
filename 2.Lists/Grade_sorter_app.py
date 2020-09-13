# The Grade Sorter app

# write a program that will collect four grades from a user and the program will sort the grades from highest to lowest. Then the program will simulate t=dropping the lowest two grades the user entered . Lastly, it will comment on the users highest grade

# greet the user
print("Welcome to the grade sorter app")

# create a blank list called grades
grades = []

# get the user input to add four grades to the list
first_grade = int(input("What is your First Grade (0-100):"))
grades.append(first_grade)
second_grade = int(input("What is your Second Grade (0-100):"))
grades.append(second_grade)
third_grade = int(input("What is your Third Grade (0-100):"))
grades.append(third_grade)
fourth_grade = int(input("What is your Fourth Grade (0-100):"))
grades.append(fourth_grade)

# print unsorrted list of grades
print("\nYour grades are:" + str(grades))

# display the sorrted list, highest to lowest
grades.sort(reverse=True)
print("\nYour Grades from Highest to Lowest are:" + str(grades))

# remove the last two grades and print them by assigning them after removal
removed_grade = grades.pop()
print("\nThe Lowest two Grades will now be dropped.")
print("Removed grade:" + str(removed_grade))

# perform the same operation again to remove another grade from the back of the list
removed_grade = grades.pop()
print("\nRemoved grade:" + str(removed_grade))

# print the remaning grades
print("Your remaning grades are:" + str(grades))

# display the grade in first index to show the highest grade
print("Nice Work! Your highest grade is a " + str(grades[0]))

# the exercise covers list methods like append , pop, sort and sort in reverse and also accessing the list using the index
