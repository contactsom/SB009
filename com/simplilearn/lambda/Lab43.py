'''
43. Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be sorted before strings.
'''

l = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
l1=list(sorted(l, key=lambda x: str(x)))
print(l1)