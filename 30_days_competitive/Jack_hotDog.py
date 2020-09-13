# Jack brought 800 hotdogs for his school picnic. If they were contained in packages of 8 hot dogs, how many total packages does he buy?
# Create a Python program without using \  or \\ or % operator









totalHotDog = 400
totalHotDog_perpack = 8
packs = 0
while totalHotDog >= totalHotDog_perpack:
    totalHotDog += totalHotDog_perpack
    packs+=1

print( "jack bought total"+" packs")


# the logic goes this way , as we are asked not to use the div operators, we shall take  a while loop and its conditon is as long as the total hotdogs are more than the number per packet specified we should keep substracting them from the total, and at each operation the "pack " variable will be added with 1.

# this is typically what a divison does. continous substraction of specified quantity and multiplication as we know is the contionous addtion of specified qunatity..

# this problem is Pretty intresting 