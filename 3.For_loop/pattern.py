""" printing the pattern 
1 2 3 4
2 3 4
3 4
4
 """

for  n in range(1,5):
    for i in range(1,6-n):
        print(i,end=" ")
    print()
