# Miles per hour conversion app

#Write a program that will convert any given speed in miles per hour to a more metric friendly unit of miles per second. All the calculcations should be rounded to two decimal places

# Display the welcome message
print('Welcome to the Miles per hour conversion app')
# get user input of speed in miles per hour
speed=float(input('What is your speed in miles per hours:'))

# coverting the speed in miles per hour to meters per second
# 1mph = 0.4474 mps
speed_mps=(speed)*0.4474

#round the output to 2 decimal places using round function 
print('Your speed in meters per second is',round(speed_mps,2))