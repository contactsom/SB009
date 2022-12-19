'''
6. Write a Python program to square and cube every number in a given list of integers using Lambda.
'''

lint = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square = list(map(lambda x : x ** 2, lint))
print(square)

cube = list(map(lambda x: x ** 3, lint))
print(cube)