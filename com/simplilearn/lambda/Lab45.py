'''
46. Write a Python program to count the occurrences of the items in a given list using lambda.
'''
l = [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
for i,j in enumerate(set(l)):
    print((l[i], l.count(i)))

