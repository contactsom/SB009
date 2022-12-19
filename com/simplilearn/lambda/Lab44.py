'''
44. Write a Python program to sort a given list of strings(numbers) numerically using lambda.
'''
l = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
l1=list(sorted(l , key = lambda x : int(x)))
print(l1)
