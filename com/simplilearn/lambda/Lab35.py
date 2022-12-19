'''
36. Write a Python program to remove all elements from a given list present in another list using lambda.
'''

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [2, 4, 6, 8]
l3=list(filter(lambda x : x not in l2 ,l1))
print(l3)