""" Factorial Calculator App """

# write a program that will calculate the factorial of any given number . Your program will display the mathematical relationship of the factorial. It will then use the math library to compute the value of the given factorial. Lastly, your program will use its own algorithm to compute the value of the given factorial and compare the results .
import math as m

# greet the user
print("Welcome to the Factorial calculator app.")

# get the use input for the number they want to print.
number = int(input("\nWhat number would you like to compute the factoria of?  "))

print(str(number) + "!=", end=" ")
for n in range(1, number):
    print(str(n) + str("*"), end="")
print(str(number))

# compute factorial using inbuilt function
fact = m.factorial(number)
print("Here is the result form the math library: ")
print("The factorial of " + str(number) + " is " + str(fact))

# compute generally now
print('\n Here is the result from own Algorithm: ')
fact_2=1
for i in range(1,number+1):
    fact_2=fact_2*i
print("The factorial of " + str(number) + " is " + str(fact_2))

