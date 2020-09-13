# help a teacher to display the entire  multiplication table of a given number

#Take the user input for the number
print('Welcome to the multiplication table program') 
number=int(input('\nEnter the Number:'))
limit=int(input('\nEnter the number till which you want to print the table '))

# print the table for the given number using the for loop
for t in range(limit+1):
    print(str(number)+' * '+str(t)+' = '+str(number*t))

print('End of the multiplication table')

#modification:
""" Should try to print without displaying for t as '0' """