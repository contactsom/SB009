'''
41. Write a Python program to find index position and value of the maximum and minimum values in a given list of numbers using lambda.
'''

l = [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
l1=max(enumerate(l), key=lambda x: x[1])
print(l1)

l2=min(enumerate(l), key = lambda x : x[1])
print(l2)