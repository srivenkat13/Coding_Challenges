# print a double sided stair case or pyramid  for the user based on the number of lines asked

# define a function for that purpose which takes the number of lines as an input

def pattern(n):
    k= 2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range( 0, i+1):
            print('*', end=" ")
        print("\r")

pattern(5)