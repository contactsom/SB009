'''
25. Write a Python program to sort a given list of lists by length and value using lambda.
'''
l = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
l1=sorted(l, key = lambda x: (len(x),x))
print(l1)
