'''
29. Write a Python program to count float number in a given mixed list using lambda.
'''
l = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
l1=list(filter(lambda x: type(x) == float, l))
print(l1)