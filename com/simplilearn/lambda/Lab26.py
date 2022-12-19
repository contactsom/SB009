'''
26. Write a Python program to find the maximum value in a given heterogeneous list using lambda.
'''
l = ['Python', 3, 2, 4, 5, 'version']
l1=max(list(filter(lambda x : isinstance(x, int), l)))
print(l1)