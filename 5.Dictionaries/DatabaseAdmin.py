# write a program that will simulate logging into a databaase and prompting a user to change their password. All usernames and passwords to the database will be stored in a dictonary. Upon entering the correct credentials, your program will prompt the user to enter a new password that is a minimum of 8 characters, if the lenght is shorter reject it. If the user who logged in is the admin, a list of all usernames and passwords need to be displayed.

# printing the welcome message
print("Welcome to the Database Admin System Program")

# creating a dictonary
log_on_information = {
    "jonas": "martha33",
    "ulrich": "hannah123",
    "martha": "jonas33",
    "thanous": "myson",
    "admin00": "adammikkel",
}
# get user input for the username
user=input('Enter the username: ')

# check if the user name is in the dictonary
if user in log_on_information.keys():
    password=input('Enter your password: ')
    if password == log_on_information[user]:
        print('\n Hello '+user+' ! You\'re logged in.')
        if user == 'admin00':
            #display whole dict
            print('\n Here is the current user database:')
            for key, value in log_on_information.items():
                print(' Usernaem: '+key+'\t Password :'+value)
        else:
            passwordChange=input('Would you like to change your password (yes/no)').lower().strip()
            if passwordChange == 'yes':
                newPassword=input("What would you llike your new password to be (min 8 characters): ")
                if len(newPassword)>=8:
                    log_on_information[user]==newPassword
                else:
                    print('Entered password is not up to 8 characters')
            else:
                print('\n Thank you !')
    else:
        print('Password Incorrect')
else:
    print(" You ain't on the system bro !")
