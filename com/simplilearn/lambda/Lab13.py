'''
13. Write a Python program to find the values of length six in a given list using Lambda.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
l=list(filter(lambda x : len(x) == 6 , weekdays))
print(l)