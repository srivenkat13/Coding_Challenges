""" Fibonacci Calculator App """

# write a program that will compute the first n terms of the fibonnaci sequence and display the terms. Next , your program will calculate the rations of consecutive Fibonacci numbers to prove that these ratios approach the irrational mathematical constant pi; 1.618...

# greet the user
print("Welcome to the Fibonacci Calculator App")

# get the user input for the number of digits they want to compute
number = int(
    input("\n How many digits of the Fibonacci Seequence would you like to compute: ")
)
# printing the fibonacci series 
fibonacci=[1,1]
for i in range(number-2): # as the list already has two elements , we take the range till number-2 but not number.
    new=fibonacci[i]+fibonacci[i+1]
    fibonacci.append(new)

# dislaying the values of the fibonacci list.
print('\nThe first '+ str(number) +' numbers of the Fibonnaci Sequence are: ')
for number in fibonacci:
    print(number)


# printing the consecutive ratios in the fibonnaci series 
ratio_list=[]
# write a for loop that will compute the ratio of alternative terms and then append it to the ratio list
# here the range is given as one less than lenght of the fibonnaci because , the ratios for a series of length 5 would be just 4
for r in range(len(fibonacci)-1):
    ratio=fibonacci[r+1]/ fibonacci[r]
    ratio_list.append(ratio)

#display the golden ratio values 
print('\nThe Corresponding  golden ratio values are: ')
for r in ratio_list:
    print(r)


print("\n The ratio of consecutive Fibonacci terms approaches phi")