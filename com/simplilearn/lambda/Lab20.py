'''
21. Write a Python program that multiply each number of given list with a given number using lambda function. Print the result.
'''

l = [2, 4, 6, 9, 11]
l1=list(map(lambda x : x * 2, l))
print(l1)