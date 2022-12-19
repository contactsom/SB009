'''
39. Write a Python program to calculate the average value of the numbers in a given tuple of tuples using lambda.
'''

t = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
t1=tuple(map(lambda x : sum(x) / float(len(x)), zip(*t)))
print(t1)