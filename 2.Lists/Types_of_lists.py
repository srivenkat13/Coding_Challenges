# Different types of lists program

# write a program that will highlight the similarities and differences between four different types of lists : a list of strings,  a list of intergers, a list of floats, and a list of lists. For each list, your program will describe the data type of the list, the elements of the listm and the data type of the first element of the list. The program will then highlightm the similarities and differences between sorting alist numerically and alphabetically..


# print the welcome message
print("\t\tSummary Table")

# define the   lists in hard code method
num_strings = ["15", "100", "55", "42"]
num_ints = [15, 100, 55, 42]
num_floats = [15.5, 100.4, 55.9, 42.3]
num_lists=[[1,2,3],[4,5,6],[7,8,9,]]

# printing the summary of the string list
print('\nThe variable num_strings is a'+ str(type(num_strings)))
print('It contians the elements:'+str(num_strings))
print('The element '+str(num_strings[0])+'is a '+str(type(num_strings[0])))

print('\nThe variable num_ints is a'+ str(type(num_ints)))
print('It contians the elements:'+str(num_ints))
print('The element '+str(num_ints[0])+'is a '+str(type(num_ints[0])))

print('\nThe variable num_floats is a'+ str(type(num_floats)))
print('It contians the elements:'+str(num_floats))
print('The element '+str(num_floats[0])+'is a '+str(type(num_floats[0])))

print('\nThe variable num_lists is a'+ str(type(num_lists)))
print('It contians the elements:'+str(num_lists))
print('The element '+str(num_lists[0])+'is a '+str(type(num_lists[0])))


# sort and print the ints and strings lists
print('\nNow sorting the num_strins and num_ints.....')


num_strings.sort()
num_ints.sort()
print('Sorted num_strings:'+ str(num_strings ))
print('Sorted num_ints:'+ str(num_ints ))

# closing message
print('\nStrings are sorted alphabetically sorted while integers are sorted numerically!')