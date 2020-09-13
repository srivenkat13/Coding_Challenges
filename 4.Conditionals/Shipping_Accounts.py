""" Shipping Accounts program """

# write a program that will simulate logging into a business's shipping accounts software. Once logged in your program will display the current costs of shipping x amount of items. Based on the number of items shippedm the cost to ship each item will vary. Once the cost to ship an item is set, your program will calculate the cost of shipping the entire order. Upon Confirmation of the order, your program will place the order and prepare the shipment

# create a list that will hold 5 user names of your choice
user_names = ["venkat", "sai", "sri", "raj", "hazel"]

# greet the user
print("Welcome to the Shipping Accounts Program")

# get the user input for the user name
user = input("Hello, what is your username ").strip().lower()

# define the shipping details as a function
def ship():
    print("Current Shipping prices are as follows: ")
    print("\n Shipping orders 0 to 100: \t\t $ 5.10 each")
    print("\n Shipping orders 100 to 500: \t\t $ 5.00 each")
    print("\n Shipping orders 500 to 1000: \t\t $ 4.95 each")
    print("\n Shipping orders over 1000: \t\t $ 4.80 each")


# if the user name is in the list of user_names welcome the user
if user in user_names:
    print("Hello " + str(user) + ". Welcome back to your account.")
    ship() # printing those chunk of statments 
    items = int(input("\n How many items would you like to ship:"))
    if items > 0 and items < 100:
        print(
            "To Ship "
            + str(items)
            + " items it would cost you $"
            + str(round((items * 5.10), 2))
            + " at $5.10 per item"
        )
    elif items >= 100 and items < 500:
        print(
            "To Ship "
            + str(items)
            + " items it would cost you $"
            + str(round((items * 5.00), 2))
            + " at $5.00 per item"
        )
    elif items >= 500 and items < 1000:
        print(
            "To Ship "
            + str(items)
            + " items it would cost you $"
            + str(round((items * 4.95), 2))
            + " at $4.95 per item"
        )
    else:
        print(
            "To Ship "
            + str(items)
            + " items it would cost you $"
            + str(round((items * 4.80), 2))
            + " at $4.80 per item"
        )
        # placing the oder based upon the user request
    confirm = input(" Would you like to place the order(Y/N): ").strip().lower()
    if confirm =="y":
        print(" Okay, Shipping your " + str(items) + " items")
    else:
        print(" Fine, the order is cancelled.")

# if the user if not present in the system
else:
    print("You ain't on the system bro")

