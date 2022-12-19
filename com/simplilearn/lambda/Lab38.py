'''
38. Write a Python program to calculate the product of a given list of numbers using lambda.
'''
from functools import reduce
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1=reduce(lambda x,y : x*y, l)

print(l1)