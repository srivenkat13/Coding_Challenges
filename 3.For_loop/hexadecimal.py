""" Binary Hexadecimal Converter app """

# write a program that will generate binary and hexadecimal values from 1 upto a specified user value. your program will use list slicing to to first only show a portioin of these  values. and then loop through the entire list  of decimal, binary and hexadecimal values to show the relationship between numbers of different bases.

# print the welcome message
print("Welcome to the binary to hexadecimal converter app")

# seek the user input for number of values they would like to covert
limit = int(
    input("Compute binary and hexadecimal values up to the  following decimal number: ")
)

# generate a list  of decimal numbers using the  range function
# as the range function doesnt include the last digit we here take it as limit+1
deci = list(range(1, limit + 1))

# creating blank lists for binary and hexadecimal values
binary = []
hexa = []

for i in deci:
    binary.append(bin(i))
    hexa.append(hex(i))
print("Generating the lists......Complete!")

# use slicing to show the portion of each list  and user input for the same
start = int(input(" What decimal number would you like to start at: "))
stop = int(input(" What decimal number would you like to stop at: "))

# print the numbers from the given range
print("Binary values from " + str(start) + " to " + str(stop) + " :")
for i in binary[
    start - 1 : stop
]:  # here -1 is given for start as the start value is user input but when slicing its the index
    print(i)

print("\nHexadecimal values from " + str(start) + " to " + str(stop) + " :")
for i in hexa[start - 1 : stop]:
    print(i)

# generate the entire list now, by prompting the user to press enter
input("Press Enter to see all values from 1 to " + str(limit))

# print the entire table
print("Decimal----Binary----Hexadecimal")
print("--------------------------------")
for d,b,h in zip(deci,binary,hexa):
    print( str(d)+'\t'+ str(b)+'\t\t'+str(h))
print(" I have displayed your entire table.")

# this program gives good idea of zip function, itterating trhough a list, printing list from the give slice 