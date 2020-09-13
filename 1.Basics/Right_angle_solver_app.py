import math as m

# The Right Triangle Solver App

# Write a program to calculate the hypotenuse and area of a right angle triangle given its two sides. Round all the calculations to 3 decimal places and provide the summary of the mathematical results

# greet the user with welcome message
print("Welcome to the Right Triangle Solver App")

# get the user input for the first side of the triangle
first = float(input("What is the first side of the Triangle:"))

# get the user input for the second side of the triangle
second = float(input("What is the second side of the Triangle:"))

# find the lenght of hypotenuse using the sqrt() math function
hypotenuse = m.sqrt((first ** 2) + (second ** 2))
hypotenuse = round(hypotenuse, 3)

# calculate the area of the triangle from the sides above
area = 0.5 *( first * second)
area = round(area, 3)

# display the results of hypotenuse and area
print(
    "For a triangle with legs of"
    + str(first)
    + "and"
    + str(second)
    + "the hypotenuse is"
    + str(hypotenuse)
)
print(
    "For a triangle with legs of"
    + str(first)
    + "and"
    + str(second)
    + "the area is"
    + str(area)
)

