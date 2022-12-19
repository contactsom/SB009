'''
27. Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda.
'''

l = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
l1=sorted(l, key = lambda x : sum(x))
print(l1)