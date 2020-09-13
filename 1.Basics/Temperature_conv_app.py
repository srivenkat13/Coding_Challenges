# The Temperature Conversion App

# Write a program that will convert a give temperature in Fahrenheit to Celsius and Kelvin. All the decimal places are rounded to 4 decimal places. Lastly, the results are displayed in table style format

# greet the welcome message
print("Welcome to the Temperature Conversion App")

# get the user input in fahrenheit, with decimal places
fahrenheit = float(input("What is the give temperature in degrees Fahrenheit:"))

# converting into celsius and kelvin 
celsius=(fahrenheit-32)/1.8
celsius=round(celsius,4)
kelvin=celsius+273.15

# print such that they are all alligned 
print("\nFahrenheit:\t"+str(fahrenheit))
print("Celsius:\t"+str(celsius))
print("Kelvin:\t\t"+str(kelvin))

# modification: Ask the scale they are giving in and convert to rest 
# modification2: ask the scale they are giving in and scale they want to convert into 