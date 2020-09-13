""" Quadratic Equation Solver app """
# write a program that will display the solution to any number of the quadtratic equations . your program will ask the user for how many quadractic equations they like to solve, ask for the coefficients of the equation in the standard form of ax^2 +bx +c=0, solve for x and then display the solution. The program need to allow both real and complex solutions .
import math, cmath
# print the welcome summary to the user.
print("Welcome to the Quadratic Equation Solver App.")
print("\n A quadratic equation is of the form ax^2 + bx + c = 0 ")
print("Your solutions can be real or complex numbers.")
print(" A complex number has two parts : a + bj")
print(" Where 'a' is the real part and 'bj' is the imaginary portion")

# get the user input for the number of equations they want to solve.
limit = int(input("How many equations would you like to solve now: "))

# loop through the itterations given by the user
for i in range(limit):
    print("Solving Equation # " + str(i + 1))
    print('----------------------------')
    # get the user input for the coefficients of the quadratic equations
    a = float(input("Enter your value of a (coefficient of x^2): "))
    b = float(input("Enter your value of b (coefficient of x ): "))
    c = float(input("Enter your value of c (constant): "))
    print('\n The solutions to '+str(a)+'x^2 + '+str(b)+'x + '+str(c)+' = 0 are:')
    #  solving the quadratic equation formula
    x1= (-b + cmath.sqrt(b**2 - 4*a*c))/ (2*a )
    x2= (-b - cmath.sqrt(b**2 - 4*a*c))/ (2*a )

    print('\n \t x1 = '+ str(x1))
    print(' \t x2 = '+ str(x2))
    print('----------------------------')
print('Thank you for using the quadratic equation solver app.')