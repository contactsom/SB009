'''
19. Write a Python program to find the numbers of a given string and store them in a list,
display the numbers which are bigger than the length of the list in sorted form.
Use lambda function to solve the problem.
'''

string = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
list1 = [i for i in string.split(' ')]
numbers = sorted([int(x) for x in list1 if x.isdigit() ])
l1=list(filter(lambda x : x if x > len(numbers) else '', numbers))

print(l1)