# Grocery List app

# write a program that will simulate a grocery shopping list. The program will start with two items on the shopping list, meat and cheese and then allow a user  to add three new items to the list. To simulate shopping , your program will ask the user what item they ust purchased and them remove the item from the shopping list. Upon having only two items in the shopping list, your  program will inform the user that the store is out of particular item and prompt the user to replace the item with a new item. You will use the date time library to dispplay the current date and time the shopping is taking place in mm/dd hh:mm format.

import datetime as dt

# greet the user
print("\nWelcome to the Grocery List App")

# define the grocery list
grocery_list = ["Meat", "Cheese"]

# print the current date and time using the python library
time = dt.datetime.now()  # this displays the current time
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

print("Current Date and Time:" + month + "\\" + day + " " + hour + ":" + minute)

# display the current grocery list
print(
    "\nYou currenlty have "
    + str(grocery_list[0])
    + " and "
    + str(grocery_list[1] + " in your list.")
)

# Take input from the user for new grocery items
first = input("\nEnter the item you want to add to grocery list: ").title()
grocery_list.append(first)

second = input("Enter the item you want to add to grocery list: ").title()
grocery_list.append(second)

third = input("Enter the item you want to add to grocery list: ").title()
grocery_list.append(third)

# print the current grocery list
print("\nHere is your current grocery list:" + str(grocery_list))
# print the sorted grocery list
grocery_list.sort()
print("Here is your current grocery list sorted:" + str(grocery_list))

# simulate the shopping list
print("\nSimulating grocery shopping...")

# print the current list lenght using the len() method
print("\nCurrent grocery list: " + str(len(grocery_list)) + " items")
print(grocery_list)
# ask for the food bought by the user
purchased = input("What food did you buy: ").title()
# remove the above specified item from the list
print('Removing '+str(purchased)+' from the list.... ')
grocery_list.remove(purchased)

#removing the second item from the list
print("\nCurrent grocery list: " + str(len(grocery_list)) + " items")
print(grocery_list)
# ask for the food bought by the user
purchased = input("What food did you buy: ").title()
# remove the above specified item from the list
print('Removing '+str(purchased)+' from the list.... ')
grocery_list.remove(purchased)

#removing the third item from the list
print("\nCurrent grocery list: " + str(len(grocery_list)) + " items")
print(grocery_list)
# ask for the food bought by the user
purchased = input("What food did you buy: ").title()
# remove the above specified item from the list
print('Removing '+str(purchased)+' from the list.... ')
grocery_list.remove(purchased)

# removing the fourth item from the list
print("\nCurrent grocery list: " + str(len(grocery_list)) + " items")
print(grocery_list)
# print that the store is out of the last item in the list 
print('\nSorry the Store is out of '+str(grocery_list[-1]))
grocery_list.pop()
# ask for what to add at the end of the list instead
new=input('What food would you like instead: ').title()
grocery_list.insert(0,neworan)

# print the final list
print('\nHere is what remains on your grocery list:')
print(grocery_list)